import sqlite3
import requests
from datetime import datetime
city="Chercasy"
key = "2516d7b16bddecafc54e491f03da8399"
URL="https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
response = requests.get(URL)
weather = response.json()
connection = sqlite3.connect(database='Chercasy_Weather.sl3',timeout=5)
cursor = connection.cursor()
# cursor.execute("create table Chercasy_Weather(date_time text,temperature real );")
# connection.commit()
if 'main' in weather:
        temperature = weather['main']['temp']
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'Сьогодні: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'Температура:{city}: {temperature}°C"')
else:
    print(f"Помилка API: Не вдалося отримати дані про погоду. Повідомлення сервера: {weather.get('message', 'Немає даних про температуру.')}")




