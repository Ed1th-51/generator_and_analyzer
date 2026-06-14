import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["gender", "age", "height", "weight"]

def generate_row():

    return {
        "gender": random.choice(["man", "woman"]),
        "age": random.randint(18, 60),
        "height": random.randint(150, 200),
        "weight": round(random.uniform(40, 120), 1),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)