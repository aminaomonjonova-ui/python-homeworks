#Library Management System with Custom Exceptions

# --- Custom Exceptions ---
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


# --- Classes ---
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        library.lend_book(book.title)
        self.borrowed_books.append(book)
        book.is_borrowed = True
        print(f"{self.name} borrowed '{book.title}'")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            library.return_book(book.title)
            print(f"{self.name} returned '{book.title}'")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def lend_book(self, title):
        if title not in self.books:
            raise BookNotFoundException(f"The book '{title}' does not exist.")
        book = self.books[title]
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{title}' is already borrowed.")
        book.is_borrowed = True

    def return_book(self, title):
        if title in self.books:
            self.books[title].is_borrowed = False


# --- Testing the system ---
try:
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_book(book1)
    library.add_book(book2)

    member1 = Member("Alice")

    member1.borrow_book(book1, library)
    member1.borrow_book(book2, library)
    member1.return_book(book1, library)

    # Trigger an exception
    member1.borrow_book(book1, library)
    member1.borrow_book(book1, library)  # Should raise BookAlreadyBorrowedException

except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print("Error:", e)


#Student Grades Management (CSV)
Name,Subject,Grade
Alice,Math,85
Bob,Science,78
Carol,Math,92
Dave,History,74

import csv

# --- Read data from grades.csv ---
grades = []
with open('grades.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row)

# --- Calculate average grade per subject ---
subject_totals = {}
subject_counts = {}

for row in grades:
    subject = row['Subject']
    grade = int(row['Grade'])
    subject_totals[subject] = subject_totals.get(subject, 0) + grade
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

average_grades = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# --- Write averages to average_grades.csv ---
with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade'])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 2)])

print("average_grades.csv file created successfully!")



#JASON HANDLING

[
    {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
]


import json
import csv

# --- Load tasks from JSON ---
with open('tasks.json', 'r') as file:
    tasks = json.load(file)

# --- Display all tasks ---
print("\nAll Tasks:")
for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# --- Calculate task statistics ---
def task_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    avg_priority = sum(t['priority'] for t in tasks) / total
    return total, completed, pending, avg_priority

total, completed, pending, avg_priority = task_stats(tasks)
print("\n--- Task Statistics ---")
print(f"Total tasks: {total}")
print(f"Completed tasks: {completed}")
print(f"Pending tasks: {pending}")
print(f"Average priority: {round(avg_priority, 2)}")

# --- Save any changes back to JSON ---
with open('tasks.json', 'w') as file:
    json.dump(tasks, file, indent=4)

# --- Convert JSON data to CSV ---
with open('tasks.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
    for task in tasks:
        writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

print("\ntasks.csv file created successfully!")


