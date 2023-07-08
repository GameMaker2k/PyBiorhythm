import math
from datetime import datetime

def calculate_biorhythm(birth_date: datetime, target_date: datetime) -> dict:
    diff = target_date - birth_date
    days = diff.days

    biorhythms = {
        "Physical": math.sin(2 * math.pi * days / 23),
        "Emotional": math.sin(2 * math.pi * days / 28),
        "Intellectual": math.sin(2 * math.pi * days / 33),
        "Average": (math.sin(2 * math.pi * days / 23) + math.sin(2 * math.pi * days / 28) + math.sin(2 * math.pi * days / 33)) / 3,
        "Spiritual": math.sin(2 * math.pi * days / 53),
        "Intuition": math.sin(2 * math.pi * days / 38),
        "Awareness": math.sin(2 * math.pi * days / 48),
        "Aesthetic": math.sin(2 * math.pi * days / 43)
    }

    return biorhythms

def get_date_from_user(prompt: str) -> datetime:
    date_str = input(prompt)
    return datetime.strptime(date_str, "%Y-%m-%d")

def main():
    print("Biorhythm Calculator")
    birth_date = get_date_from_user("Enter your birth date (YYYY-MM-DD): ")
    target_date = get_date_from_user("Enter the target date (YYYY-MM-DD): ")

    biorhythms = calculate_biorhythm(birth_date, target_date)

    for name, value in biorhythms.items():
        print(f"{name}: {value:.2f}")

if __name__ == "__main__":
    main()
