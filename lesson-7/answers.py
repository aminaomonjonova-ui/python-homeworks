#Generalized Vector Class 
import math 

class Vector :
    #create a vector from any number of components 
    def __str__(self, *components):
        self.components = list (components)

    #show vector as a string 
    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    
    #check if two vectors have the same size
    def _check_dimension(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension!")
    
    # add two vectors  
    def __add__(self, other):
        self._check_dimension(other)
        result = [ a + b for a, b in zip(self.components, other.components) ]
        return Vector(*result)
    
    # subtract two vectors
    def __sub__(self, other):
        self._check_dimension(other)
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*result)
    
    # dot product *
    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum (a * b for a, b in zip(self.components, other.components))
        else:
            #scalar multiplication
            result = [a * other for a in self.components] 
            return Vector(*result)
        
    # for scalar * vector 
    def __rmul__(self, other):
        return self.__mul__(other)
    
    # find magnitude 
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    
    # normalize 
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("cannot normalize a zero vector.")
        normalized = [ a / mag for a in self.components ]
        return Vector (*normalized )
    
#Employee records manager 
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name 
        self.position = position 
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
    
class EmployeeManager:
    FILE_NAME = "employees.txt"

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        #check for unique id 
        if self.search_emloyee(emp_id, show=False):
            print("employee ID already exists!")
            return
        
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{emp_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = file.readlines()
                if not data:
                    print("No emloyees found. ")
                else:
                    print("Employee records:")
                    for line in data:
                        print(line.strip())
        except FileNotFoundError:
            print("No employee file found yet.")

    def search_employee(self, emp_id, show=True):
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    if line.startswith(emp_id + ","):
                        if show:
                            print("Employee Found:", line.strip())
                        return line.strip()
            if show:
                print("Employee not found.")
            return None
        except FileNotFoundError:
            print("No records yet.")
            return None

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        lines = []
        found = False

        try:
            with open(self.FILE_NAME, "r") as file:
                lines = file.readlines()

            with open(self.FILE_NAME, "w") as file:
                for line in lines:
                    if line.startswith(emp_id + ","):
                        found = True
                        name = input("Enter new name: ")
                        position = input("Enter new position: ")
                        salary = input("Enter new salary: ")
                        file.write(f"{emp_id},{name},{position},{salary}\n")
                    else:
                        file.write(line)

            if found:
                print("Employee updated successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("no records found.")

        def delete_employee(self):
            emp_id = input("enter employee ID to delete:")
            lines = []
            found = False

            try:
                with open(self.FILE_NAME, "r") as file:
                    lines = file.readlines()

                with open(self.FILE_NAME, "w") as file:
                    for line in lines:
                        if not line.startswith(emp_id + ","):
                            file.write(line)
                        else:
                            found = True
                if found:
                    print("✅ Employee deleted successfully!")
                else:
                    print("❌ Employee not found.")

            except FileNotFoundError:
                print("No records yet.") 

        def menu(self):
            while True:
                print("\n--- Employee Records Manager ---")
                print("1. Add new employee")
                print("2. View all employees")
                print("3. Search employee")
                print("4. Update employee")
                print("5. Delete employee")
                print("6. Save tasks")
                print("7. Exit")

                choice = input("enter your choice:")

                if choice == "1":
                    self.add_employee()
                elif choice == "2":
                    self.view_all_employees()
                elif choice == "3":
                    emp_id = input("enter employee ID to search : ")
                    self.search_employee(emp_id)
                elif choice == "4":
                    self.update_employee()
                elif choice == "5":
                    self.delete_employee()
                elif choice == "6":
                    self.save_tasks()
                elif choice == "7":
                    print("goodbye!")
                    break
                else:
                    print("invalid choice, please try again.") 


#to do application 
import json
import csv
import os

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

# File Handlers
class JSONStorage:
    FILE_NAME = "tasks.json"

    def save(self, tasks):
        with open(self.FILE_NAME, "w") as file:
            json.dump([t.to_dict() for t in tasks], file, indent=2)

    def load(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r") as file:
            data = json.load(file)
            return [Task(**d) for d in data]


class CSVStorage:
    FILE_NAME = "tasks.csv"

    def save(self, tasks):
        with open(self.FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for t in tasks:
                writer.writerow(t.to_dict())
    def load(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r")as file:
            reader = csv.DictReader(file)
            return [Task(**row)for row in reader]
        
# Main To-Do Manager
class ToDoManager:
    class ToDoManager:
        def __init__(self, storage):
            self.storage = storage
            self.tasks = self.storage.load()

        def add_task(self):
            t_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            desc = input("Enter Description: ")
            due = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            self.tasks.append(Task(t_id, title, desc, due, status))
            print("Task added successfully!")
        
        def view_tasks(self):
            if not self.tasks:
                print("No tasks yet.")
            else:
                print("\nTasks:")
                for t in self.tasks:
                    print(t)

        def update_task(self):
            t_id = input("Enter Task ID to update: ")
            for t in self.tasks:
                if t.task_id == t_id:
                    t.title = input("New Title: ")
                    t.description = input("New Description: ")
                    t.due_date = input("New Due Date: ")
                    t.status = input("New Status: ")
                    print("Task updated!")
                    return
            print("Task not found.")

        def delete_task(self):
            t_id = input("Enter Task ID to delete: ")
            self.tasks = [t for t in self.tasks if t.task_id != t_id]
            print("Task deleted!")

        def filter_tasks(self):
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
            for t in filtered:
                print(t)

        def save_tasks(self):
            self.storage.save(self.tasks)
            print("Tasks saved successfully!") 

        def menu(self):
            while True:
                print("\n--- To-Do Application ---")
                print("1. Add a new task")
                print("2. View all tasks")
                print("3. Update a task")
                print("4. Delete a task")
                print("5. Filter tasks by status")
                print("6. Save tasks")
                print("7. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.view_tasks()
                elif choice == "3":
                    self.update_task()
                elif choice == "4":
                    self.delete_task()
                elif choice == "5":
                    self.filter_tasks()
                elif choice == "6":
                    self.save_tasks()
                elif choice == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice, try again.")  