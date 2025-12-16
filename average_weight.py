import csv
from datetime import date, datetime, timedelta

FILE_NAME = "weights.csv"

# ================= SAVE DATA =================
def save_weight(weight):
    today = date.today()
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([today, weight])
    print("✅ Weight saved successfully")

# ================= READ DATA =================
def read_data():
    data = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append([datetime.strptime(row[0], "%Y-%m-%d").date(), float(row[1])])
    except FileNotFoundError:
        pass
    return data

# ================= MAX & MIN =================
def max_min_weight():
    data = read_data()
    if not data:
        print("❌ No data available")
        return

    weights = [row[1] for row in data]
    print(f"⬆️ Highest weight: {max(weights)} kg")
    print(f"⬇️ Lowest weight: {min(weights)} kg")

# ================= WEEKLY REPORT =================
def weekly_report():
    data = read_data()
    today = date.today()
    start = today - timedelta(days=7)

    weekly = [w for d, w in data if start <= d <= today]

    if not weekly:
        print("❌ No data for this week")
        return

    print("\n📊 Weekly Report")
    print(f"Average: {sum(weekly)/len(weekly):.2f} kg")
    print(f"Highest: {max(weekly)} kg")
    print(f"Lowest: {min(weekly)} kg")

# ================= WEEKLY COMPARISON =================
def weekly_comparison():
    data = read_data()
    today = date.today()

    current_start = today - timedelta(days=7)
    previous_start = today - timedelta(days=14)
    previous_end = today - timedelta(days=8)

    current = [w for d, w in data if current_start <= d <= today]
    previous = [w for d, w in data if previous_start <= d <= previous_end]

    if not current or not previous:
        print("❌ Not enough data for weekly comparison")
        return

    diff = (sum(current)/len(current)) - (sum(previous)/len(previous))
    print(f"📈 Weekly change: {diff:+.2f} kg")

# ================= MONTHLY REPORT =================
def monthly_report():
    data = read_data()
    today = date.today()

    monthly = [w for d, w in data if d.month == today.month and d.year == today.year]

    if not monthly:
        print("❌ No data for this month")
        return

    print("\n📊 Monthly Report")
    print(f"Average: {sum(monthly)/len(monthly):.2f} kg")
    print(f"Highest: {max(monthly)} kg")
    print(f"Lowest: {min(monthly)} kg")

# ================= MONTHLY COMPARISON =================
def monthly_comparison():
    data = read_data()
    today = date.today()

    this_month = [(d, w) for d, w in data if d.month == today.month and d.year == today.year]

    last_month_date = today.replace(day=1) - timedelta(days=1)
    last_month = [(d, w) for d, w in data if d.month == last_month_date.month and d.year == last_month_date.year]

    if not this_month or not last_month:
        print("❌ Not enough data for monthly comparison")
        return

    diff = (sum(w for _, w in this_month)/len(this_month)) - (sum(w for _, w in last_month)/len(last_month))
    print(f"📈 Monthly change: {diff:+.2f} kg")

# ================= MAIN MENU =================
while True:
    print("\n1️⃣ Add weight")
    print("2️⃣ Weekly report")
    print("3️⃣ Monthly report")
    print("4️⃣ Highest & lowest weight")
    print("5️⃣ Weekly comparison")
    print("6️⃣ Monthly comparison")
    print("7️⃣ Exit")

    choice = input("Choose option: ")

    if choice == "1":
        weight = float(input("Enter weight (kg): "))
        save_weight(weight)

    elif choice == "2":
        weekly_report()

    elif choice == "3":
        monthly_report()

    elif choice == "4":
        max_min_weight()

    elif choice == "5":
        weekly_comparison()

    elif choice == "6":
        monthly_comparison()

    elif choice == "7":
        print("👋 Goodbye")
        break

    else:
        print("❌ Invalid choice")
