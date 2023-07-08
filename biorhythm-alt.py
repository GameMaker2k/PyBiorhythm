import math
from datetime import datetime

def calculate_biorhythm(birth_date: datetime, target_date: datetime) -> tuple:
    diff = target_date - birth_date
    days = diff.days

    physical = math.sin(2 * math.pi * days / 23)
    emotional = math.sin(2 * math.pi * days / 28)
    intellectual = math.sin(2 * math.pi * days / 33)

    return physical, emotional, intellectual

def get_date_from_user(prompt: str) -> datetime:
    date_str = input(prompt)
    return datetime.strptime(date_str, "%Y-%m-%d")

def main():
    print("Biorhythm Calculator")
    birth_date = get_date_from_user("Enter your birth date (YYYY-MM-DD): ")
    target_date = get_date_from_user("Enter the target date (YYYY-MM-DD): ")

    physical, emotional, intellectual = calculate_biorhythm(birth_date, target_date)

    print(f"\nPhysical: {physical:.2f}")
    print(f"Emotional: {emotional:.2f}")
    print(f"Intellectual: {intellectual:.2f}")

if __name__ == "__main__":
    main()
