import csv
from datetime import date, datetime, timedelta

def save_data(cost , reason) :
    today = date.today()
    with open('expenses.csv','a',newline='',encoding='UTF-8') as file :
        writer = csv.writer(file)
        writer.writerow([today,cost,reason])

def read_data():
    data=[]
    with open('expenses.csv','r',encoding='utf-8') as file :
        reader = csv.reader(file)
        for row in reader :
            data.append(row)
    return data

def show_by_period(start_date,end_date):
    data=read_data()
    total=0

    for row in data :
        row_data=datetime.strptime(row[0], "%Y-%m-%d").date()
        if start_date <= row_data <= end_date :
            print(f"Date: {row[0]} | cost: {row[1]} | Reason: {row[2]}")
            total+= int(row[1])

    print(f"total cost = {total}")

def monthly_report(month,year):
    total = 0
    print(f"\nmonthly Report for {month}/{year}\n")
    with open("expenses.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader :
            date_obj=datetime.strptime(row[0], "%Y-%m-%d")
            if date_obj.month == month and date_obj.year == year:
                print(f"{row[0]} | {row[1]} | {row[2]}")
                total +=int(row[1])
    print(f"\nTotal expenses = {total}")


operation =input("1- Add expense\n2- Show expenses\n3- monthly report\n4-Monthly money management\nChoose: ")

today=date.today()

if operation == "1":

    cost=int (input("Enter cost : "))
    reason=input("Enter reason : ")

    save_data(cost,reason)

    print("Saved successfully ✅")

elif operation=="2":
    choice=input("1- one day\n2- Last week\n3- Custom period\nchoose: ")
    if choice == "1":
        d = input ("Enter date (YYYY-MM-DD): ")
        d=datetime.strptime(d,"%Y-%m-%d").date()
        show_by_period(d,d)
    
    elif choice == "2" :
        start = today - timedelta(days=7)
        show_by_period(start,today)
    
    elif choice=="3" :
     
        start = today - timedelta(days=29)
        monthly_report(start, today)
   
    else:
        print("Invalid choice❌")

elif operation == "3":
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    monthly_report(month, year)
elif operation == '4' :
        m=int (input ("Enter money total: "))
        o=int (input("Enter total youer responsibilities: "))
        net = m-o
        charity=net*(5/100)
        luxuries=net*(15/100)
        personal_expenses=net*(50/100)
        saving = net*(30/100)
        print(f"Net money = {net}\nPersonal Expenses = {personal_expenses}\nLuxuries = {luxuries}\nCharity = {charity}\nSaving = {saving}\nGoodluck ")
    
else:
    print("Invalid choice❌")