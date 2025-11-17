# task 1 
from bs4 import BeautifulSoup

# ---- 1. Load & Parse HTML ----
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.select("table tbody tr")

weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.replace("°C", "").strip())
    condition = cols[2].text.strip()

    weather_data.append({
        "day": day,
        "temp": temp,
        "condition": condition
    })

# ---- 2. Display Weather Data ----
print("5-Day Weather Forecast:\n")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temp']}°C, {entry['condition']}")

# ---- 3. Highest Temperature ----
max_temp = max(entry["temp"] for entry in weather_data)
hottest_days = [entry["day"] for entry in weather_data if entry["temp"] == max_temp]

print("\nDay(s) with highest temperature:", hottest_days)

# ---- Sunny Days ----
sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]
print("Sunny day(s):", sunny_days)

# ---- 4. Average Temperature ----
avg_temp = sum(entry["temp"] for entry in weather_data) / len(weather_data)
print("\nAverage temperature:", round(avg_temp, 2), "°C")


# task 2 
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"

# ---- Database Setup ----
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    UNIQUE(title, company, location)
)
""")
conn.commit()

# ---- Scrape Job Listings ----
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="description").text.strip()
    apply_link = job.find("a", text="Apply")["href"]

    try:
        # Try insert new job
        cursor.execute("""
        INSERT INTO jobs (title, company, location, description, apply_link)
        VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, apply_link))
    except sqlite3.IntegrityError:
        # Job exists → check if content changed
        cursor.execute("""
        SELECT description, apply_link
        FROM jobs
        WHERE title=? AND company=? AND location=?
        """, (title, company, location))

        old_desc, old_link = cursor.fetchone()

        if old_desc != description or old_link != apply_link:
            cursor.execute("""
            UPDATE jobs
            SET description=?, apply_link=?
            WHERE title=? AND company=? AND location=?
            """, (description, apply_link, title, company, location))

conn.commit()

print("Scraping & database update completed.")

# ---- Filtering ----
def filter_jobs(location=None, company=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location=?"
        params.append(location)
    if company:
        query += " AND company=?"
        params.append(company)

    df = pd.read_sql_query(query, conn, params=params)
    return df

# ---- Export to CSV ----
def export_jobs_to_csv(filename, location=None, company=None):
    df = filter_jobs(location, company)
    df.to_csv(filename, index=False)
    print("Exported to", filename)

#task 3
import json
import requests

# Load laptops page 1
resp1 = requests.post("https://api.demoblaze.com/bycat", json={"cat": "notebook"})
page1 = resp1.json()["Items"]

# Load laptops page 2
resp2 = requests.post("https://api.demoblaze.com/bycat", json={"cat": "notebook", "id": "9"})
page2 = resp2.json()["Items"]

all_items = page1 + page2

laptops = []

for item in all_items:
    laptops.append({
        "name": item["title"],
        "price": item["price"],
        "description": item["desc"]
    })

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4)

print("Saved laptops.json successfully!")

#i hope i did it right 
