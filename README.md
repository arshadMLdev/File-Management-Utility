# 🗂️ File Management Utility

> A lightweight, zero-dependency Python utility that automatically organizes files in any directory into neatly categorized subfolders — saving you time and keeping your workspace clutter-free.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Supported File Types](#supported-file-types)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Example](#example)
- [Customization](#customization)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## 📖 Overview

The **File Management Utility** is a command-line Python tool designed to help you bring order to disorganized folders. Whether it's your Downloads folder, a cluttered Desktop, or a shared project directory — this utility scans the target folder and automatically moves files into categorized subdirectories based on their file extensions.

It handles edge cases gracefully: hidden files are ignored, existing subdirectories are skipped, files with unknown extensions are grouped into an `Others` folder, and files that already exist at the destination are left untouched to prevent accidental overwrites. At the end of every run, a clean summary report tells you exactly how many files were moved per category.

---

## ✨ Features

- **Automatic categorization** — Files are sorted into folders like `Images`, `Documents`, `Data`, `Audio`, `Videos`, `Archives`, `Code`, `Fonts`, and `Others` based on their extension.
- **Summary report** — After every run, a formatted breakdown shows how many files were moved into each category and how many were skipped.
- **Safe operation** — Files already present at the destination path are never overwritten.
- **Hidden file protection** — Files beginning with `.` (e.g., `.DS_Store`, `.gitignore`) are automatically skipped.
- **Directory-aware** — Subdirectories inside the target folder are left completely untouched.
- **Extensible mapping** — The file-type dictionary is easy to modify, making it simple to add new categories and extensions.
- **No external dependencies** — Built entirely with Python's standard library (`os` and `shutil`).
- **Clear terminal feedback** — Every file move is logged to the console in real time.

---

## 📂 Supported File Types

| Category | Extensions |
|----------|------------|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp` |
| Documents | `.txt`, `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx` |
| Data | `.csv`, `.xlsx`, `.xls`, `.json`, `.xml` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg` |
| Videos | `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.webm` |
| Archives | `.zip`, `.tar`, `.rar`, `.7z`, `.gz`, `.bz2` |
| Code | `.py`, `.js`, `.html`, `.css`, `.ts`, `.jsx`, `.tsx`, `.java`, `.c`, `.cpp`, `.cs`, `.php`, `.rb`, `.go`, `.sh`, `.sql` |
| Fonts | `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot` |
| Others | *(any unrecognized extension)* |

> You can easily extend this list — see the [Customization](#customization) section.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.6** or higher
- No third-party packages required

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/file-management-utility.git
cd file-management-utility
```

2. **Verify Python is installed:**

```bash
python --version
```

That's it — no virtual environments or package installations needed.

### Usage

Run the script from your terminal:

```bash
python main.py
```

You will be prompted to enter the path to the folder you want to organize:

```
Enter the folder path: /Users/arshad/Downloads
```

The utility will then scan the folder, move files into their respective category subfolders, and print a summary report at the end:

```
Moved: resume.pdf → Documents
Moved: photo_2024.jpg → Images
Moved: sales_data.csv → Data
Moved: podcast_episode.mp3 → Audio
Moved: demo_video.mp4 → Videos
Moved: project_backup.zip → Archives
Moved: index.html → Code
Moved: helvetica.ttf → Fonts
Moved: random_file.xyz → Others
Skipped (already exists): old_notes.txt

========================================
         ORGANIZATION SUMMARY
========================================
  Archives        1 file(s)
  Audio           1 file(s)
  Code            1 file(s)
  Data            1 file(s)
  Documents       1 file(s)
  Fonts           1 file(s)
  Images          1 file(s)
  Others          1 file(s)
  Videos          1 file(s)
----------------------------------------
  Total moved     9 file(s)
  Skipped         1 file(s)
========================================
```

---

## ⚙️ How It Works

The utility follows a simple, linear workflow:

1. **Input validation** — The user-provided path is checked with `os.path.exists()` and `os.path.isdir()` to confirm it points to a real, accessible directory.
2. **Directory scan** — `os.listdir()` retrieves all entries in the folder.
3. **Filtering** — Each entry is checked: hidden files (starting with `.`) and subdirectories (`os.path.isdir()`) are skipped.
4. **Extension detection** — `os.path.splitext()` extracts the file extension, which is normalized to lowercase.
5. **Category lookup** — The extension is matched against the `file_types` dictionary using `.get()`. If no match is found, the file is assigned to the `Others` category.
6. **Destination creation** — `os.makedirs(..., exist_ok=True)` creates the target subfolder if it doesn't already exist.
7. **Safe move** — `os.path.exists()` checks whether the file already exists at the destination before calling `shutil.move()`, preventing overwrites.
8. **Summary report** — After all files are processed, a formatted table displays the count of files moved per category and the total skipped count.

---

## 🗃️ Project Structure

```
file-management-utility/
│
├── main.py   # Main script
└── README.md           # Project documentation
```

After running the utility on a folder, the output structure will look something like this:

```
target-folder/
│
├── Images/
├── Documents/
├── Data/
├── Audio/
├── Videos/
├── Archives/
├── Code/
├── Fonts/
└── Others/
```

---

## 🧪 Example

**Before running the utility:**

```
Downloads/
├── invoice_march.pdf
├── profile_photo.png
├── dataset_2024.csv
├── meeting_notes.txt
├── background_music.mp3
├── demo_reel.mp4
├── project_backup.zip
├── index.html
├── helvetica.ttf
└── setup_installer.exe
```

**After running the utility:**

```
Downloads/
├── Documents/
│   ├── invoice_march.pdf
│   └── meeting_notes.txt
├── Images/
│   └── profile_photo.png
├── Data/
│   └── dataset_2024.csv
├── Audio/
│   └── background_music.mp3
├── Videos/
│   └── demo_reel.mp4
├── Archives/
│   └── project_backup.zip
├── Code/
│   └── index.html
├── Fonts/
│   └── helvetica.ttf
└── Others/
    └── setup_installer.exe
```

---

## 🛠️ Customization

To add support for new file types or categories, simply edit the `file_types` dictionary at the top of `main.py`:

```python
file_types = {
    # Add a new extension to an existing category
    '.tiff': 'Images',

    # Or create a brand new category
    '.epub': 'Ebooks',
    '.mobi': 'Ebooks',
}
```

No other changes to the script are required. The new category folder will be created automatically on the next run.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements — such as recursive folder support, a GUI, undo functionality, or a config file for custom mappings — feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

---

## 👤 Author

**Arshad**

- GitHub: [@arshadMLdev](https://github.com/arshadMLdev)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
