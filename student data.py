import csv

def save_data(name,grades,age):
    
    with open("student_Data.csv",'a',newline='', encoding="UTF-8") as file:
        writer=csv.writer(file)
        writer.writerow([name , age , grades])


def read_data():
    data=[]
    with open("student_Data.csv",'r', encoding="UTF-8") as file:
        reader= csv.reader(file)
        for row in reader :
            data.append(row)
        return data

order = input("1-Add student\n2-show students\n3-search\n choose: ")

if order == '1':
    name = input("Enter student name: ")
    grades =  float (input("Enter grade: "))
    age = float(input("Entar age: "))
    save_data(name,age,grades)
    print("Saved successfully ✅")
elif order == '2' :
    data = read_data()
    print(data)
else:
     print("Invalid choice❌")