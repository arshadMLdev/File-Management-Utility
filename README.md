# 🗂️ File Management Utility

> A lightweight, zero-dependency Python utility that automatically organizes files in any directory into neatly categorized subfolders — saving you time and keeping your workspace clutter-free.

---

## 📌 Table of Contents:

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

It handles edge cases gracefully: hidden files are ignored, existing subdirectories are skipped, files with unknown extensions are grouped into an `Others` folder, and files that already exist at the destination are left untouched to prevent accidental overwrites.

---

## ✨ Features

- **Automatic categorization** — Files are sorted into folders like `Images`, `Documents`, `Data`, `Audio`, and `Others` based on their extension.
- **Safe operation** — Files already present at the destination path are never overwritten.
- **Hidden file protection** — Files beginning with `.` (e.g., `.DS_Store`, `.gitignore`) are automatically skipped.
- **Directory-aware** — Subdirectories inside the target folder are left completely untouched.
- **Extensible mapping** — The file-type dictionary is easy to modify, making it simple to add new categories and extensions.
- **No external dependencies** — Built entirely with Python's standard library (`os` and `shutil`).
- **Clear terminal feedback** — Every file move is logged to the console in real time.

---

## 📂 Supported File Types

| Extension | Category |
|-----------|----------|
| `.jpg`, `.png` | Images |
| `.txt`, `.pdf` | Documents |
| `.csv`, `.xlsx` | Data |
| `.mp3`, `.wav` | Audio |
| *(anything else)* | Others |

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
python file_organizer.py
```

You will be prompted to enter the path to the folder you want to organize:

```
Enter the folder path: /Users/arshad/Downloads
```

The utility will then scan the folder and move files into their respective category subfolders, printing a log of every action taken:

```
Moved: report.pdf → Documents
Moved: photo_2024.jpg → Images
Moved: sales_data.csv → Data
Moved: podcast_episode.mp3 → Audio
Moved: random_file.zip → Others
```

---

## ⚙️ How It Works

The utility follows a simple, linear workflow:

1. **Input validation** — The user-provided path is checked with `os.path.exists()` and `os.path.isdir()` to confirm it points to a real, accessible directory.
2. **Directory scan** — `os.listdir()` retrieves all entries in the folder.
3. **Filtering** — Each entry is checked: hidden files (starting with `.`) and subdirectories (`os.path.isdir()`) are skipped.
4. **Extension detection** — `os.path.splitext()` extracts the file extension, which is normalized to lowercase.
5. **Category lookup** — The extension is matched against the `file_types` dictionary. If no match is found, the file is assigned to the `Others` category.
6. **Destination creation** — `os.makedirs(..., exist_ok=True)` creates the target subfolder if it doesn't already exist.
7. **Safe move** — `os.path.exists()` is used to check whether the file already exists at the destination before calling `shutil.move()`, preventing overwrites.

---

## 🗃️ Project Structure

```
file-management-utility/
│
├── file_organizer.py   # Main script
└── README.md           # Project documentation
```

After running the utility on a folder, the output structure will look something like this:

```
target-folder/
│
├── Images/
│   ├── photo.jpg
│   └── screenshot.png
│
├── Documents/
│   ├── notes.txt
│   └── resume.pdf
│
├── Data/
│   ├── report.csv
│   └── budget.xlsx
│
├── Audio/
│   └── recording.mp3
│
└── Others/
    └── archive.zip
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
└── Others/
    └── setup_installer.exe
```

---

## 🛠️ Customization

To add support for new file types or categories, simply edit the `file_types` dictionary at the top of `file_organizer.py`:

```python
file_types = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',        # ← Add new extensions like this
    '.txt': 'Documents',
    '.pdf': 'Documents',
    '.docx': 'Documents',    # ← Add a new extension to an existing category
    '.csv': 'Data',
    '.xlsx': 'Data',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.mp4': 'Videos',        # ← Or create an entirely new category
    '.mov': 'Videos',
    '.zip': 'Archives',      # ← Another new category
    '.tar': 'Archives',
}
```

No other changes to the script are required.

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

- GitHub:(https://github.com/arshadMLdev)

---
