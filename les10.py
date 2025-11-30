import requests
import sqlite3
from datetime import  datetime

connection = sqlite3.connect(database="weather.sl3", timeout=5)
cursor = connection.cursor()

# cursor.execute("create table city_weather(date_time text,city text, description text,temp real,feels_like real,humidity integer);")
# connection.commit()



key = "2516d7b16bddecafc54e491f03da8399"
def save(weather):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = weather['weather'][0]['main']
    temp = weather['main']['temp']
    feels_like = weather['main']['feels_like']
    humidity = weather['main']['humidity']
    cursor.execute(f"""INSERT INTO city_weather (date_time, city, description, temp, feels_like, humidity) VALUES
        ('{current_datetime}', '{city}', '{description}', '{temp}', '{feels_like}', '{humidity}');""")
    connection.commit()
def show_all():
    cursor.execute(f"SELECT * FROM city_weather;")
    connection.commit()

    weathers = cursor.fetchall()
    for weather in weathers:
        print(weather)

while True:
    city=input("City:")
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric').json()

    save(weather)
    show_all()

    print(weather)
    if input("Continue? (y/n): ").lower() == "n":
        break

