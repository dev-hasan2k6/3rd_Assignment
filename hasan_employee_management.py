#employee add korar function

def add_employee(name, em_id, salary):
    line = f"{name} | {em_id} | {salary}\n"
    with open("employees.txt", "a") as f:
        f.write(line)

#employee dekhar function

def view_employees():
    with open ("employees.txt", "r") as f:
        em_data = f.read()
        if em_data == "":
            return "No employee records found."
    return em_data

#menu

while True:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

#input newa and input jachai kora

    choice=input("Choose Option: ").strip()
    
    if choice =="1":
        name = input("\nEnter Name: ")
        em_id = input("Enter ID: ")
        try:
            salary = int(input("Enter Salary: "))
            add_employee(name, em_id, salary)
            print()
            print("Employee Added Successfully")
            print()
        except ValueError:
            print("\nPlease type a number only\n")
       
    elif choice == "2":
        try:
            print(view_employees())
        except FileNotFoundError:
            print("\nFile not found. Please add an employee first.\n")
    elif choice == "3":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please choose 1, 2, or 3.\n")
