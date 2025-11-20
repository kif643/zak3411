import sqlite3
connection=sqlite3.connect(database="kif_4kbase.sl3",timeout=5)
cursor= connection.cursor()
print(connection)
print(cursor)

# cursor.execute("CREATE TABLE students (id integer primary key not null,full_name text, birth_year integer,avg_score real,coins inteher,crystals integer);")
# cursor.execute("""INSERT INTO students (id, full_name, birth_year, avg_score, coins, crystals) VALUES
# (1, 'Іван Петренко',       2005, 8.7, 120, 4),
# (2, 'Марія Коваль',        2006, 9.1, 300, 10),
# (3, 'Олег Сидоренко',      2004, 7.5, 80, 2),
# (4, 'Анна Левченко',       2005, 9.8, 540, 13),
# (5, 'Дмитро Шевченко',     2007, 6.9, 50, 1),
# (6, 'Софія Дяченко',       2006, 8.3, 200, 5),
# (7, 'Артем Гнатюк',        2004, 7.2, 100, 2),
# (8, 'Катерина Бойко',      2005, 9.4, 430, 11),
# (9, 'Максим Коваленко',    2006, 8.1, 170, 3),
# (10,'Олександра Романюк',  2005, 9.0, 350, 9);
# """ )
year=input("birthyear:")
coins=input("coins:")
cursor.execute(f"SELECT * FROM students WHERE birth_year={year} and coins={coins}")
connection.commit()
all=cursor.fetchall()
for student in all:
    print(student)

connection.close()
