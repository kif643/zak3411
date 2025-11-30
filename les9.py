import sqlite3

connection = sqlite3.connect(database="itstep.sl3", timeout=5)

cursor = connection.cursor()

# CREATE TABLE
# cursor.execute("CREATE TABLE students (id integer primary key not null, full_name text, birth_year integer, avg_score real, coins integer, crystals integer);")

# INSERT DATA
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
# """)
def add():
    id=int(input("id:"))
    full_name=(input("full_name:"))
    birth_year=(input("birth_year:"))
    avg_score=float(input("avg_score:"))
    coin = int(input("coins: "))
    crystal=int(input("crystal: "))

    cursor.execute(f"""INSERT INTO students
                (id,full_name,birth_year,avg_score,coins,crystals) VALUES
                ({id},{full_name},{birth_year},{avg_score},{coin},{crystal});""")
connection.commit()

def delete():
    id=int(input("id:"))
    cursor.execute(f"DELETE FROM students where id={id}")
    connection.commit()

def show_all():
    cursor.execute(f"SELECT * FROM students;")
    connection.commit()

    students = cursor.fetchall()
    for student in students:
        print(student)
def menu():
    print("::::STUDENTS::::")
    print("1) add new")
    print("2) show all")
    print("3) delete")
    print("4) exit")
while True:
    menu()
    choose=(input("choose:"))
    if choose=="1":
        add()
    elif choose=="2":
        show_all()
    elif choose=="3":
        delete()
    elif choose=="4":
        break
    else:
        print("wrong choice!!!!!!!")

connection.close()