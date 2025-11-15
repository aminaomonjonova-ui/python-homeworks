import requests  # for sending HTTP requests

API_KEY = "73f59a0351b00c45dbf95590a86735d1"  # your API key
CITY = "Tashkent"

# Create the API request URL
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Send a request to the API
response = requests.get(URL)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    print(f"Weather in {CITY}:")
    print(f" Temperature: {data['main']['temp']}°C")
    print(f" Feels like: {data['main']['feels_like']}°C")
    print(f" Humidity: {data['main']['humidity']}%")
    print(f" Description: {data['weather'][0]['description'].capitalize()}")
else:
    print("Error:", data.get("message", "Unable to fetch weather data."))

#i couldnt get my API key, the website is giving 404 error
import requests
import random

API_KEY = "my API key"

# Получаем список жанров
genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
genres = requests.get(genre_url).json()['genres']

# Показываем пользователю все жанры
for g in genres:
    print(g['id'], "-", g['name'])

genre_id = input("\nВведи номер жанра: ")

# Получаем фильмы по жанру
movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US&page=1"
movies = requests.get(movies_url).json()['results']

# Случайный фильм
movie = random.choice(movies)
print("\n Рекомендация фильма:")
print("Название:", movie['title'])
print("Описание:", movie['overview'])
print("Дата выхода:", movie['release_date'])
