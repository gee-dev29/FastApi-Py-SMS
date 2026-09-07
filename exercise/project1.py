# from pathlib import Path
# import csv
# BASE_DIR = Path(__file__).resolve().parent
# DIR_PATH = BASE_DIR / "exercise" / "files"

# FILE_CATEGORIES = {
#     "images": [".jpg", ".jpeg", ".png", ".gif"],
#     "documents": [".pdf", ".docx", ".txt"],
#     "data": [".csv", ".json"],
#     "presentations": [".pptx", ".ppt"],
# }
# for dirpath in DIR_PATH.iterdir():
#     if dirpath.is_file():
#         if dirpath.suffix in FILE_CATEGORIES["images"]:
#             mkdir = mkdir(DIR_PATH / "images", parents=True, exist_ok=True)
#             Path(dirpath).rename(DIR_PATH / "images" / dirpath.name)
#         elif dirpath.suffix in FILE_CATEGORIES["documents"]:
#             mkdir = mkdir(DIR_PATH / "documents", parents=True, exist_ok=True)
#             Path(dirpath).rename(DIR_PATH / "documents" / dirpath.name)
#         elif dirpath.suffix in FILE_CATEGORIES["data"]:
#             mkdir = mkdir(DIR_PATH / "data", parents=True, exist_ok=True)
#             Path(dirpath).rename(DIR_PATH / "data" / dirpath.name)
#         elif dirpath.suffix in FILE_CATEGORIES["presentations"]:
#             mkdir = mkdir(DIR_PATH / "presentations", parents=True, exist_ok=True)
#             Path(dirpath).rename(DIR_PATH / "presentations" / dirpath.name)
#         else:
#             mkdir = mkdir(DIR_PATH / "unknown", parents=True, exist_ok=True)
#             Path(dirpath).rename(DIR_PATH / "unknown" / dirpath.name)
