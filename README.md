🧬 MetaMorphMasker



Created by david-marin-0xff



MetaMorphMasker is a lightweight Python desktop application for editing and removing metadata from image files (JPEG, PNG, and TIFF).

Built with CustomTkinter, it helps users visualize metadata, remove EXIF tags for privacy, or modify fields interactively.



⚙️ Features



&nbsp;Image metadata viewer — Detects and lists all EXIF tags (camera model, GPS, timestamps, etc.).



&nbsp;Edit metadata — Modify or update EXIF fields manually.



&nbsp;Remove metadata — Strip all metadata to reduce file size and protect privacy.



&nbsp;Backup system — Automatically creates .bak copies before modifications.



&nbsp;Custom save location — Choose where backups are stored.



&nbsp;Help Page — Explains supported formats, usage, and credits.



&nbsp;Dark red theme — Minimalist and easy on the eyes.



🧰 Tech Stack



Python 3.11+



CustomTkinter — Modern GUI



Pillow (PIL) — Image processing



Piexif — EXIF metadata manipulation



🧑‍💻 How It Works



When a user loads an image, MetaMorphMasker:



Reads EXIF data via piexif.load()



Displays detected tags in a structured view



Allows inline editing or full metadata stripping



Creates a backup file before any write operation



Saves a clean or updated version of the image



All operations are done locally — no data leaves your machine.





&nbsp;Setup

git clone https://github.com/david-marin-0xff/MetaMorphMasker.git

cd MetaMorphMasker

python -m venv venv

.\\venv\\Scripts\\activate

pip install customtkinter pillow piexif

python metamorphmasker.py



🧾 Supported Formats



JPEG (.jpg, .jpeg)



PNG (.png)



TIFF (.tif, .tiff)





