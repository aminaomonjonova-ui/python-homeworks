#task1
from bs4 import BeautifulSoup

# ---------- 1. PARSE HTML FILE ----------
with open("weather.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = soup.select("table tbody tr")

weather = []

for row in rows:
    day = row.find_all("td")[0].get_text(strip=True)
    temp = int(row.find_all("td")[1].get_text(strip=True).replace("°C", ""))
    condition = row.find_all("td")[2].get_text(strip=True)

    weather.append({"day": day, "temp": temp, "condition": condition})

# ---------- 2. DISPLAY WEATHER DATA ----------
print("=== 5-Day Weather Forecast ===")
for entry in weather:
    print(f"{entry['day']}: {entry['temp']}°C, {entry['condition']}")

# ---------- 3. FIND SPECIFIC DATA ----------
max_temp = max(w["temp"] for w in weather)
hottest_days = [w["day"] for w in weather if w["temp"] == max_temp]

sunny_days = [w["day"] for w in weather if w["condition"] == "Sunny"]

print("\nHottest day(s):", hottest_days)
print("Sunny day(s):", sunny_days)

# ---------- 4. AVERAGE TEMPERATURE ----------
average_temp = sum(w["temp"] for w in weather) / len(weather)
print("\nAverage temperature:", round(average_temp, 2), "°C")

#task2
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    UNIQUE(title, company, location)
)
""")
conn.commit()


# ---------------- SCRAPING FUNCTION ----------------
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.find_all("div", class_="card-content")

    for card in job_cards:
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        description = card.find("div", class_="description").text.strip()
        apply_link = card.find("a", text="Apply")["href"]

        try:
            cursor.execute("""
            INSERT INTO jobs (title, company, location, description, apply_link)
            VALUES (?, ?, ?, ?, ?)
            """, (title, company, location, description, apply_link))

        except sqlite3.IntegrityError:
            # Job exists — check for updates
            cursor.execute("""
            SELECT description, apply_link FROM jobs
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
    print("Job scraping and incremental update complete.")


# ---------------- FILTERING FUNCTION ----------------
def filter_jobs(location=None, company=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location=?"
        params.append(location)
    if company:
        query += " AND company=?"
        params.append(company)

    return pd.read_sql_query(query, conn, params=params)


# ---------------- EXPORT FUNCTION ----------------
def export_to_csv(filename, location=None, company=None):
    df = filter_jobs(location, company)
    df.to_csv(filename, index=False)
    print("Exported to:", filename)


# Run the scraper
scrape_jobs()


#task 3
import json
import requests

# ---------------- LOAD PAGE 1 ----------------
page1 = requests.post(
    "https://api.demoblaze.com/bycat",
    json={"cat": "notebook"}
).json()["Items"]

# ---------------- LOAD PAGE 2 (Next button data) ----------------
page2 = requests.post(
    "https://api.demoblaze.com/bycat",
    json={"cat": "notebook", "id": "9"}
).json()["Items"]

items = page1 + page2

laptops = []

for item in items:
    laptops.append({
        "name": item["title"],
        "price": item["price"],
        "description": item["desc"]
    })

# ---------------- SAVE TO JSON ----------------
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4)

print("Saved laptops.json")
