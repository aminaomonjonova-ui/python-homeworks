import sqlite3

# -----------------------
# 1. CREATE DATABASE
# -----------------------
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# -----------------------
# 2. INSERT DATA
# -----------------------
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data)
conn.commit()

# -----------------------
# 3. UPDATE DATA
# Change Jadzia Dax → Ezri Dax
# -----------------------
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()

# -----------------------
# 4. QUERY DATA
# Species = Bajoran
# -----------------------
print("Bajoran characters:")
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# -----------------------
# 5. DELETE CHARACTERS OVER 100 YEARS OLD
# -----------------------
cursor.execute("DELETE FROM Roster WHERE Age > 100")
conn.commit()

# -----------------------
# 6. BONUS — Add Rank column
# -----------------------
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

# Update ranks
cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
cursor.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")
conn.commit()

# -----------------------
# 7. ADVANCED QUERY — sort by Age DESC
# -----------------------
print("\nCharacters sorted by age (descending):")
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


import sqlite3

# -----------------------
# 1. CREATE DATABASE
# -----------------------
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# -----------------------
# 2. INSERT DATA
# -----------------------
books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]

cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books)
conn.commit()

# -----------------------
# 3. UPDATE YEAR
# Update 1984 → 1950
# -----------------------
cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")
conn.commit()

# -----------------------
# 4. QUERY DATA
# Genre = Dystopian
# -----------------------
print("\nDystopian books:")
cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

# -----------------------
# 5. DELETE books before 1950
# -----------------------
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
conn.commit()

# -----------------------
# 6. BONUS — Add Rating column
# -----------------------
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")
conn.commit()

# -----------------------
# 7. ADVANCED QUERY — sort by Year ascending
# -----------------------
print("\nBooks sorted by Year:")
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


