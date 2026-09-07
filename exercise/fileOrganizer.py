
from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent
DIR_PATH = BASE_DIR / "exercise" / "files"

FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "data": [".csv", ".json"],
    "presentations": [".pptx", ".ppt"],
}

for dirPath in DIR_PATH.iterdir():
    if dirPath.is_file():
        target_folder = "unknown"
        for category, extentions in FILE_CATEGORIES.items():
            if dirPath.suffix.lower() in extentions:
                target_folder = category
                break

        dest_dir = DIR_PATH / target_folder
        dest_dir.mkdir(parents=True, exist_ok=True)
        dirPath.rename(dest_dir / dirPath.name)
