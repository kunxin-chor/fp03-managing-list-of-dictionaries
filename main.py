def main():
  # empty list to store all the employee
  employees = []

  while True:
    print("------------------------------")
    display_menu()
    choice = int(input("Enter choice: "))
    if choice==1:
      add_new_staff(employees)
    elif choice==2:
      save_employees(employees)
    elif choice==3:
      load_employees(employees)
    elif choice==4:
      show_employees(employees)
    elif choice==5:
      break

def show_employees(employees):
  for e in employees:
    print(e)

def add_new_staff(employees):
  name = input("Enter name: ")
  department = input("Enter department: ")
  employees.append({
    "name": name,
    "department": department
  })

  print("New employee added")
  for e in employees:
    print(e)

def save_employees(employees):
  file_ptr = open("employees.csv", "w")
  for e in employees:
    file_ptr.write(e["name"] + "," + e["department"]+"\n")
  # closing a file tells Python that you are done
  # processing it
  file_ptr.close()

def load_employees(employees):
  file_ptr = open("employees.csv", "r")
  while True:
    # strip will remove characters like spaces and \n
    # from the end of the string
    each_line = file_ptr.readline().strip()
    if not each_line:
      # we have reached end of file (EOF)
      break

    chunks = each_line.split(",")
    # chunks[0] will be the name
    # chunks[1] will be the department
    new_employee = {
      "name": chunks[0],
      "department": chunks[1]
    }

    employees.append(new_employee)
      

def display_menu():
  print("1. Add")
  print("2. Save")
  print("3. Load")
  print("4. List All")
  print("5. Quit")

main()