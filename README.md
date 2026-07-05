# 📥 Download Scripts Collection

This repository contains a set of handy Python scripts for downloading content from popular platforms. All scripts are designed to be simple, command‑line driven, and work out‑of‑the‑box with a standard Python virtual environment.

---

## 🛠️ Included Scripts

| Script | Purpose | How to Use |
|--------|---------|------------|
| `downloadyoutube.py` | Download YouTube videos listed in **download.txt** and convert them to MP3 files. | `python downloadyoutube.py` (make sure `download.txt` contains one YouTube URL per line). |
| `downloadgdrive.py` | Recursively download every file from a **public** Google Drive folder. | `python downloadgdrive.py "https://drive.google.com/drive/folders/<folder_id>"` or run the script and paste the folder link when prompted. |
| `create_venv.py` *(optional)* | Helper to create a Python virtual environment (`venv`). | `python create_venv.py [venv_folder]` |

---

## 📦 Dependencies

All required third‑party packages are listed in **requirements.txt**. Install them with:

```bash
pip install -r requirements.txt
```

> **Note:** `yt-dlp` and `ffmpeg` are required for the YouTube downloader. Install `yt‑dlp` via `pip install yt-dlp`.  `ffmpeg` must be available on your system path (download from https://ffmpeg.org or install via your OS package manager).

---

## 📂 Project Structure

```
downloadyoutube/
├── download.txt          # List of YouTube URLs (one per line)
├── downloadyoutube.py    # YouTube → MP3 downloader
├── downloadgdrive.py     # Google Drive public folder downloader
├── create_venv.py        # (optional) script to set up a virtual environment
├── requirements.txt      # Python package list for the project
├── .gitignore           # Git ignore file
└── README.md            # This documentation
```

---

## 🚀 Quick Start

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python create_venv.py
   # Activate the venv
   # Windows: venv\Scripts\activate
   # Unix/macOS: source venv/bin/activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the desired script**:
   - YouTube downloader:
     ```bash
     python downloadyoutube.py
     ```
   - Google Drive folder downloader:
     ```bash
     python downloadgdrive.py "https://drive.google.com/drive/folders/<your_folder_id>"
     ```

---

## 📝 License

This collection is released under the **MIT License** – feel free to use, modify, and share it.
