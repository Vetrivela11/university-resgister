
import json
import os

import csv

DATA_FOLDER = "data"


def save_students(students):
    os.makedirs(DATA_FOLDER, exist_ok=True)

    with open(os.path.join(DATA_FOLDER, "students.json"), "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    file_path = os.path.join(DATA_FOLDER, "students.json")

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        return json.load(file)






def save_registrations(registrations):
    os.makedirs(DATA_FOLDER, exist_ok=True)

    file_path = os.path.join(DATA_FOLDER, "registrations.csv")

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["student_id", "course_id", "status"]
        )

        writer.writeheader()
        writer.writerows(registrations)


def load_registrations():
    file_path = os.path.join(DATA_FOLDER, "registrations.csv")

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
