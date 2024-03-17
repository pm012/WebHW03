# The first part for threading (read details and instructions in README.md)
import sys
import re
import os
import shutil
from pathlib import Path
import threading

EXTENSIONS = {
    "images": [".JPG", ".JPEG", ".PNG", ".SVG"],
    "video": [".MP4", ".AVI", ".MKV", ".MOV"],
    "documents": [".DOCX", ".PDF", ".XLSX", ".PPTX", ".TXT", ".DOC"],
    "audio": ['.MP3', '.OGG', '.WAV', '.AMR'],
    "archives": ['.ZIP', '.TAR', '.GZ'],
}

# Normalization function
def normalize(file_name: str) -> str:
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    res = re.sub(r"(?u)[^\w.]", "_", file_name.translate(TRANS))
    return res

# Get category based on extension
def get_category(extension: str) -> str:
    for category, extensions_list in EXTENSIONS.items():
        if extension.upper() in extensions_list:
            return category
    return "unknown"

# Handle a folder's contents
def handle_folder(folder_path: str):
    known_extensions = set()
    unknown_extensions = set()
    files_by_category = {category: [] for category in EXTENSIONS.keys()}

    for path in Path(folder_path).iterdir():
        if path.is_file():
            _, file_extension = os.path.splitext(path)
            file_extension_upper = file_extension.upper()
            category = get_category(file_extension_upper)

            if category != "unknown":
                category_path = Path(root_path) / category
                category_path.mkdir(parents=True, exist_ok=True)
                files_by_category[category].append(path.name)
                known_extensions.add(file_extension_upper)

                if category == 'archives':
                    normalized = path.parent / normalize(path.name)
                    shutil.move(str(path), str(normalized))
                    archive_folder = category_path / normalize(path.stem)
                    archive_folder.mkdir(exist_ok=True)
                    try:
                        shutil.unpack_archive(str(normalized), str(archive_folder))
                    except Exception as e:
                        print(f"Error unpacking archive {normalized}: {e}")
                    finally:
                        os.remove(normalized)
                else:
                    shutil.move(str(path), str(category_path / normalize(path.name)))
            elif category == "unknown":
                unknown_category_path = Path(root_path) / category
                unknown_category_path.mkdir(parents=True, exist_ok=True)
                unknown_extensions.add(file_extension_upper)
                shutil.move(str(path), str(unknown_category_path / normalize(path.name)))

        else:
            if not (path.name in EXTENSIONS and root_path == str(path.parent)) and str(root_path) + "/" + "archives" != str(
                    path.parent):
                # Traverse subfolders in parallel using threading
                subfolder_thread = threading.Thread(target=handle_folder, args=(str(path),))
                subfolder_thread.start()

            if not any(path.iterdir()):
                path.rmdir()

def start():
    global root_path
    try:
        root_path = sys.argv[1]
    except Exception:
        print("Please enter a directory to sort as a command-line parameter")
        exit()

    handle_folder(root_path)
    print("Processing complete.")

if __name__ == "__main__":
    start()
