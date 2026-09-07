
import csv
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "exercise" / "files" / "warehouse_messy_data.csv"
file_path.parent.mkdir(parents=True, exist_ok=True)

messy_data = [
    ["Item_ID", "Product_Name", "Quantity", "Unit_Price", "Last_Updated"],
    ["101", "  wireless mouse ", "twenty", "$25.50", "2026/01/10"],
    ["102", "Mechanical Keyboard", "", "75.00", "01-15-2026"],
    ["103", "USB-C Hub", "15", "None", "2025.12.01"],
    ["102", "Mechanical Keyboard", "10", "75.00", "01-15-2026"],  # Duplicate
    ["104", "  HD Monitor ", "5", "$199.99", "2026-02-20"],
    ["105", "Webcam 1080p", "eight", "45.0", "InvalidDate"]
]

with open(file_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(messy_data)
print(f"Messy dataset successfully created at: {file_path}")

import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Total people in space: {data['number']}")
    print("-" * 30)
    for person in data['people']:
        print(f"- {person['name']} aboard the {person['craft']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")