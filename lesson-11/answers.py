import sqlite3

# -------------------------
# Task 1
# -------------------------

conn = sqlite3.connect("roster.db")
cur = conn.cursor()

# 1. Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Insert data
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cur.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data)

# 3. Update Jadzia → Ezri
cur.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4. Query Bajorans
print("Bajoran characters:")
cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
print(cur.fetchall())

# 5. Delete characters over 100 years
cur.execute("DELETE FROM Roster WHERE Age > 100")

# 6. Add Rank column
cur.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

# Fill Rank values
ranks = [
    ("Benjamin Sisko", "Captain"),
    ("Ezri Dax", "Lieutenant"),
    ("Kira Nerys", "Major")
]

for name, rank in ranks:
    cur.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))

# 7. Query sorted by age desc
print("\nCharacters sorted by age desc:")
cur.execute("SELECT * FROM Roster ORDER BY Age DESC")
print(cur.fetchall())

conn.commit()
conn.close()


#task 2 
import sqlite3

# -------------------------
# Task 2
# -------------------------

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# 1. Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# 2. Insert data
books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]

cur.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books)

# 3. Update 1984
cur.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")

# 4. Query Dystopian
print("\nDystopian books:")
cur.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
print(cur.fetchall())

# 5. Delete books before 1950
cur.execute("DELETE FROM Books WHERE Year_Published < 1950")

# 6. Add Rating column
cur.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

ratings = [
    ("To Kill a Mockingbird", 4.8),
    ("1984", 4.7),
    ("The Great Gatsby", 4.5)
]

for title, rating in ratings:
    cur.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

# 7. Query sorted by Year Published
print("\nBooks sorted by year asc:")
cur.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
print(cur.fetchall())

conn.commit()
conn.close()

