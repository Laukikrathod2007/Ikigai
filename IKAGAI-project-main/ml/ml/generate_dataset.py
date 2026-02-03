import csv
import random

OUTPUT_FILE = "mental_health_data_2000.csv"
TOTAL_ROWS = 2000

rows = set()

def generate_row(stress_level):
    if stress_level == "Low":
        sleep = round(random.uniform(7, 9), 1)
        study = round(random.uniform(3, 6), 1)
        screen = round(random.uniform(0.5, 3), 1)
        activity = random.randint(30, 70)
        mood = random.randint(4, 5)

    elif stress_level == "Medium":
        sleep = round(random.uniform(5.5, 7), 1)
        study = round(random.uniform(4, 7), 1)
        screen = round(random.uniform(3, 5), 1)
        activity = random.randint(15, 30)
        mood = random.randint(3, 4)

    else:  # High
        sleep = round(random.uniform(3.5, 5.5), 1)
        study = round(random.uniform(6, 9), 1)
        screen = round(random.uniform(5, 8), 1)
        activity = random.randint(0, 15)
        mood = random.randint(1, 2)

    return (sleep, study, screen, activity, mood, stress_level)


stress_distribution = (
    ["Low"] * 670 +
    ["Medium"] * 660 +
    ["High"] * 670
)

random.shuffle(stress_distribution)

while len(rows) < TOTAL_ROWS:
    stress = stress_distribution[len(rows)]
    row = generate_row(stress)
    rows.add(row)

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sleep", "study", "screen", "activity", "mood", "stress"])
    writer.writerows(rows)

print(f"✅ Dataset generated successfully: {OUTPUT_FILE}")
print(f"📊 Total rows: {len(rows)}")
