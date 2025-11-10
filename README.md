\# 🧬 MetaMorphMasker



MetaMorphMasker is a \*\*cross-format metadata inspection and editing tool\*\* built with `Python` and `CustomTkinter`.  

It allows users to \*\*view, remove, and edit metadata\*\* from images, audio, and video files through a modern dark-red GUI.



---



\##  Features



\- 🔍 \*\*Inspect metadata\*\* from multiple file types:

&nbsp; - Images (`.png`, `.jpg`, `.jpeg`, `.tiff`)

&nbsp; - Audio (`.mp3`, `.flac`, `.ogg`, `.wav`)

&nbsp; - Video (`.mp4`, `.mkv`, `.mov`, `.avi`)

&nbsp; - Text files (`.txt`)

\- ✏️ \*\*Edit\*\* and \*\*remove\*\* metadata fields

\-  \*\*Backup system\*\* — automatically creates safe copies before modifying files

\-  \*\*Smart detection\*\* using `Pillow`, `Mutagen`, and `Hachoir`

\-  \*\*Dark red custom UI\*\* using `CustomTkinter`

\-  \*\*Built-in Help page\*\* explaining usage and supported formats

\-  \*\*Portable EXE version\*\* — no Python installation required



---



\##  How It Works



1\. When you select a file, the app:

&nbsp;  - Detects its type based on the extension  

&nbsp;  - Uses different backends:

&nbsp;    - `Pillow` for image metadata (`EXIF`, `tEXt`, etc.)

&nbsp;    - `Mutagen` for audio tags (`ID3`, `FLAC`, `Ogg`)

&nbsp;    - `Hachoir` for video containers (`MP4`, `MKV`, `MOV`)

2\. Metadata is displayed in a scrollable text box.

3\. You can remove or edit tags depending on the file type.

4\. Backups are automatically created before changes.

5\. The GUI remains responsive and lightweight.



---



\##  Technologies



\- \*\*Python 3.11+\*\*

\- \*\*CustomTkinter\*\* – modern dark GUI

\- \*\*Pillow\*\* – image metadata handler

\- \*\*Mutagen\*\* – audio tag parsing/editing

\- \*\*Hachoir\*\* – binary parser for video metadata



---



\## ⚠️ Known Issues (to be debugged in next release)



\-  Audio metadata editing sometimes fails or is cumbersome — needs refinement.  

\-  Large image/audio tags like embedded album art (`APIC`) can cause slowdowns or crashes.  

\-  Some rare video formats may not display metadata properly.  

\-  No drag-and-drop support (by design).



> This is an active work-in-progress project. Debugging and contributions are welcome.



---



\##  Installation (Development)



```bash

git clone https://github.com/david-marin-0xff/MetaMorphMasker.git

cd MetaMorphMasker

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt

python metamorphmasker.py

