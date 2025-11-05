#task 1
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# Test
print(div(6, 2))  # Output: 3.0
print(div(6, 0))  # Output: "Denominator can't be zero"

#task 2 
def add_employee():
    # open file in append mode (adds to the end)
    f = open("employees.txt", "a")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    f.write(emp_id + ", " + name + ", " + position + ", " + salary + "\n")
    f.close()
    print("Employee added successfully!\n")


def view_employees():
    try:
        f = open("employees.txt", "r")
        lines = f.readlines()
        f.close()

        if len(lines) == 0:
            print("No employee records found.\n")
        else:
            print("Employee Records:\n")
            for line in lines:
                print(line.strip())
            print()
    except FileNotFoundError:
        print("File not found. Please add a record first.\n")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    try:
        f = open("employees.txt", "r")
        for line in f:
            if line.startswith(emp_id + ","):
                print("Employee found:", line.strip(), "\n")
                found = True
                break
        f.close()
        if not found:
            print("Employee not found.\n")
    except FileNotFoundError:
        print("File not found. Please add a record first.\n")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False

    try:
        f = open("employees.txt", "r")
        lines = f.readlines()
        f.close()

        f = open("employees.txt", "w")
        for line in lines:
            if line.startswith(emp_id + ","):
                print("Enter new details:")
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                f.write(emp_id + ", " + name + ", " + position + ", " + salary + "\n")
                found = True
            else:
                f.write(line)
        f.close()

        if found:
            print("Employee updated!\n")
        else:
            print("Employee not found.\n")

    except FileNotFoundError:
        print("File not found. Please add a record first.\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False

    try:
        f = open("employees.txt", "r")
        lines = f.readlines()
        f.close()

        f = open("employees.txt", "w")
        for line in lines:
            if not line.startswith(emp_id + ","):
                f.write(line)
            else:
                found = True
        f.close()

        if found:
            print("Employee deleted!\n")
        else:
            print("Employee not found.\n")

    except FileNotFoundError:
        print("File not found. Please add a record first.\n")


def main():
    while True:
        print("=== Employee Records Manager ===")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search employee by ID")
        print("4. Update employee info")
        print("5. Delete employee record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Uncomment to run:
# main()

#task 4 
import string

def create_sample_file():
    print("sample.txt not found.")
    text = input("Please type a paragraph to create it:\n")
    f = open("sample.txt", "w")
    f.write(text)
    f.close()
    print("File created!\n")

def clean_text(text):
    # Convert to lowercase and remove punctuation
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")
    return text

def word_frequency():
    try:
        f = open("sample.txt", "r")
        content = f.read()
        f.close()
    except FileNotFoundError:
        create_sample_file()
        f = open("sample.txt", "r")
        content = f.read()
        f.close()

    text = clean_text(content)
    words = text.split()
    total_words = len(words)

    # Count words manually (no collections.Counter)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Total words:", total_words)

    # Ask how many top words to show
    try:
        top_n = int(input("How many top words to show? (default 5): ") or 5)
    except:
        top_n = 5

    # Sort by frequency
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print("\nTop", top_n, "most common words:")
    for word, count in sorted_words[:top_n]:
        print(word, "-", count, "times")

    # Save to report file
    f = open("word_count_report.txt", "w")
    f.write("Word Count Report\n")
    f.write("Total Words: " + str(total_words) + "\n")
    f.write("Top " + str(top_n) + " Words:\n")
    for word, count in sorted_words[:top_n]:
        f.write(word + " - " + str(count) + "\n")
    f.close()

    print("\nReport saved to 'word_count_report.txt'.")

# Uncomment to run:
# word_frequency()

# i guess thats all, i diвте quite understand bonus task tbh 
