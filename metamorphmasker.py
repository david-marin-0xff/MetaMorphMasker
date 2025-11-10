import customtkinter as ctk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
from mutagen import File as MutagenFile
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import os
import shutil

# --- Theme ---
ctk.set_appearance_mode("dark")

RED_PRIMARY = "#8B0000"
RED_ACCENT = "#B22222"
RED_TEXT = "#FF6347"

app = ctk.CTk()
app.title("MetaMorphMasker")
app.geometry("860x540")
app.configure(fg_color=RED_PRIMARY)

# --- Functions ---
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("All Files", "*.*"),
            ("Images", "*.png;*.jpg;*.jpeg;*.tiff"),
            ("Audio", "*.mp3;*.flac;*.ogg;*.wav"),
            ("Video", "*.mp4;*.mkv;*.mov;*.avi"),
            ("Text", "*.txt"),
        ],
    )
    if not file_path:
        return

    metadata_textbox.delete("0.0", "end")
    metadata_textbox.insert("end", f"📁 File: {file_path}\n\n")
    show_metadata(file_path)


def show_metadata(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext in [".jpg", ".jpeg", ".png", ".tiff"]:
            with Image.open(file_path) as img:
                info = img.info
                if info:
                    for k, v in info.items():
                        metadata_textbox.insert("end", f"{k}: {v}\n")
                else:
                    metadata_textbox.insert("end", "No EXIF or embedded metadata found.\n")

        elif ext in [".mp3", ".flac", ".ogg", ".wav"]:
            audio = MutagenFile(file_path)
            if audio and audio.tags:
                for tag, value in audio.tags.items():
                    metadata_textbox.insert("end", f"{tag}: {value}\n")
            else:
                metadata_textbox.insert("end", "No ID3 or audio metadata found.\n")

        elif ext in [".mp4", ".mkv", ".mov", ".avi"]:
            parser = createParser(file_path)
            if not parser:
                metadata_textbox.insert("end", "Cannot parse video file.\n")
                return
            with parser:
                metadata = extractMetadata(parser)
                if metadata:
                    for item in metadata.exportPlaintext():
                        metadata_textbox.insert("end", f"{item}\n")
                else:
                    metadata_textbox.insert("end", "No video metadata found.\n")

        elif ext == ".txt":
            metadata_textbox.insert("end", "Text files typically have no embedded metadata.\n")

        else:
            metadata_textbox.insert("end", "Unsupported file type or no metadata found.\n")

    except Exception as e:
        messagebox.showerror("Error", f"Error reading metadata:\n{e}")


def remove_metadata():
    file_path = get_selected_file()
    if not file_path:
        return
    try:
        ext = os.path.splitext(file_path)[1].lower()
        backup_path = file_path + ".bak"
        shutil.copy2(file_path, backup_path)

        if ext in [".jpg", ".jpeg", ".png", ".tiff"]:
            with Image.open(file_path) as img:
                data = list(img.getdata())
                img_no_meta = Image.new(img.mode, img.size)
                img_no_meta.putdata(data)
                img_no_meta.save(file_path)
        elif ext in [".mp3", ".flac", ".ogg", ".wav"]:
            audio = MutagenFile(file_path)
            if audio and audio.tags:
                audio.delete()
                audio.save()

        metadata_textbox.insert("end", "\n✅ Metadata removed successfully.\n")
        messagebox.showinfo("Done", f"Metadata removed.\nBackup saved as:\n{backup_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Error removing metadata:\n{e}")


def edit_metadata():
    file_path = get_selected_file()
    if not file_path:
        return
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext in [".mp3", ".flac", ".ogg", ".wav"]:
            audio = MutagenFile(file_path)
            if not audio:
                messagebox.showinfo("Error", "Unsupported or unreadable audio format.")
                return

            tag_key = simpledialog.askstring("Edit Tag", "Enter the tag name (e.g., artist, title):")
            if not tag_key:
                return
            tag_value = simpledialog.askstring("Edit Tag", f"Enter new value for '{tag_key}':")
            if tag_value is not None:
                audio[tag_key] = tag_value
                audio.save()
                metadata_textbox.insert("end", f"\n🎵 Updated {tag_key} = {tag_value}\n")
                messagebox.showinfo("Success", f"Updated {tag_key}: {tag_value}")

        elif ext in [".jpg", ".jpeg", ".png", ".tiff"]:
            messagebox.showinfo("Info", "Editing image metadata is not yet supported in this version.")
        else:
            messagebox.showinfo("Info", "Editing supported for audio files only right now.")

    except Exception as e:
        messagebox.showerror("Error", f"Error editing metadata:\n{e}")


def get_selected_file():
    # Extract the file path from the top of the text box
    content = metadata_textbox.get("0.0", "1.end")
    if content.startswith("📁 File: "):
        return content.replace("📁 File: ", "").strip()
    else:
        messagebox.showwarning("No File", "Please select a file first.")
        return None


def show_help():
    help_text = """
🧬 MetaMorphMasker - Help & Info
───────────────────────────────

Supported Formats:
 • Images: JPG, JPEG, PNG, TIFF
 • Audio: MP3, FLAC, OGG, WAV
 • Video: MP4, MKV, MOV, AVI
 • Text: TXT

Features:
 - View metadata (EXIF, ID3, etc.)
 - Remove metadata (cleans hidden info)
 - Edit metadata (audio tags)
 - Backup created automatically (.bak)

Usage:
 1. Click "Select File" to load your file.
 2. View its metadata in the window.
 3. Use "Remove Metadata" to clear all tags.
 4. Use "Edit Metadata" to modify fields (audio only).

Created by david-marin-0xff
"""
    messagebox.showinfo("Help", help_text)


# --- UI Layout ---
title_label = ctk.CTkLabel(app, text="🧬 MetaMorphMasker", text_color=RED_TEXT, font=("Segoe UI", 24, "bold"))
title_label.pack(pady=20)

button_frame = ctk.CTkFrame(app, fg_color=RED_PRIMARY)
button_frame.pack(pady=10)

ctk.CTkButton(button_frame, text="Select File", width=150, fg_color=RED_ACCENT, hover_color=RED_TEXT,
              command=select_file).grid(row=0, column=0, padx=6)
ctk.CTkButton(button_frame, text="Remove Metadata", width=150, fg_color=RED_ACCENT, hover_color=RED_TEXT,
              command=remove_metadata).grid(row=0, column=1, padx=6)
ctk.CTkButton(button_frame, text="Edit Metadata", width=150, fg_color=RED_ACCENT, hover_color=RED_TEXT,
              command=edit_metadata).grid(row=0, column=2, padx=6)
ctk.CTkButton(button_frame, text="Help", width=100, fg_color="#A00000", hover_color=RED_TEXT,
              command=show_help).grid(row=0, column=3, padx=6)

metadata_textbox = ctk.CTkTextbox(app, width=780, height=330, font=("Consolas", 12))
metadata_textbox.pack(pady=20)

footer = ctk.CTkLabel(app, text="Created by david-marin-0xff", text_color="#FF9999", font=("Segoe UI", 10))
footer.pack(pady=5)

app.mainloop()
