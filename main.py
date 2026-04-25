import os
import shutil

file_types = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.txt': 'Documents',
    '.pdf': 'Documents',
    '.csv': 'Data',
    '.xlsx': 'Data',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.aac': 'Audio',
    '.m4a': 'Audio',
}

folder_path = input("Enter the folder path: ").strip()

if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
    print("Invalid folder path. Please enter a valid directory.")
else:
    for file in os.listdir(folder_path):
        if file.startswith('.'):
            continue

        full_path = os.path.join(folder_path, file)

        if os.path.isdir(full_path):
            continue

        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in file_types:
            folder_name = file_types[ext]
        else:
            folder_name = 'Others'

        destination_folder = os.path.join(folder_path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, file)

        if not os.path.exists(destination_path):
            shutil.move(full_path, destination_folder)
            print(f"Moved: {file} → {folder_name}")
