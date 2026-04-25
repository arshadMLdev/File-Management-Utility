import os
import shutil

file_types = {
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.svg': 'Images',
    '.webp': 'Images',

    # Documents
    '.txt': 'Documents',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.ppt': 'Documents',
    '.pptx': 'Documents',

    # Data
    '.csv': 'Data',
    '.xlsx': 'Data',
    '.xls': 'Data',
    '.json': 'Data',
    '.xml': 'Data',

    # Audio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.aac': 'Audio',
    '.flac': 'Audio',
    '.ogg': 'Audio',

    # Videos
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.wmv': 'Videos',
    '.flv': 'Videos',
    '.webm': 'Videos',

    # Archives
    '.zip': 'Archives',
    '.tar': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',
    '.gz': 'Archives',
    '.bz2': 'Archives',

    # Code
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.ts': 'Code',
    '.jsx': 'Code',
    '.tsx': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
    '.cs': 'Code',
    '.php': 'Code',
    '.rb': 'Code',
    '.go': 'Code',
    '.sh': 'Code',
    '.sql': 'Code',

    # Fonts
    '.ttf': 'Fonts',
    '.otf': 'Fonts',
    '.woff': 'Fonts',
    '.woff2': 'Fonts',
    '.eot': 'Fonts',
}

folder_path = input("Enter the folder path: ").strip()

if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
    print("Invalid folder path. Please enter a valid directory.")
else:
    summary = {}
    skipped = 0

    for file in os.listdir(folder_path):
        if file.startswith('.'):
            continue

        full_path = os.path.join(folder_path, file)

        if os.path.isdir(full_path):
            continue

        name, ext = os.path.splitext(file)
        ext = ext.lower()

        folder_name = file_types.get(ext, 'Others')

        destination_folder = os.path.join(folder_path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, file)

        if not os.path.exists(destination_path):
            shutil.move(full_path, destination_folder)
            print(f"Moved: {file} → {folder_name}")
            summary[folder_name] = summary.get(folder_name, 0) + 1
        else:
            print(f"Skipped (already exists): {file}")
            skipped += 1

    # Summary report
    total_moved = sum(summary.values())
    print("\n" + "=" * 40)
    print("         ORGANIZATION SUMMARY")
    print("=" * 40)

    if summary:
        for folder_name, count in sorted(summary.items()):
            print(f"  {folder_name:<15} {count} file(s)")
        print("-" * 40)
        print(f"  {'Total moved':<15} {total_moved} file(s)")
    else:
        print("  No files were moved.")

    if skipped:
        print(f"  {'Skipped':<15} {skipped} file(s)")

    print("=" * 40)
