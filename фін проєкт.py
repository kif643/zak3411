import sqlite3
import random
import colorama
from colorama import Fore
from optparse import Values

connection=sqlite3.connect(database='FBY.sl3',timeout=50)
cursor=connection.cursor()

# cursor.execute("""CREATE TABLE basketbolysti(id int, full_name text, birth_year int, shoots int, avg_score_in_school int, avg_score_in_basketball int, team_winner_or_looser text, avg_score_team int)""")
# cursor.execute("""INSERT INTO basketbolysti(id,full_name,birth_year,shoots,avg_score_in_school,avg_score_in_basketball,team_winner_or_looser,avg_score_team)VALUES
# (1,'Zakharchenko Zakhar',2013,10,11,10.2,'winner',9.1),
# (2,'Borysov Artem',2013,4,9.2,8,'winner',9.1),
# (3,'Satalov Maksym',2013,20,8,11,'winner',9.1),
# (4,'Gyranov Artem',2014,4,7,8,'winner',9.1),
# (5,'Yarik Spivak',2013,20,10,11.3,'winner',9.1),
# (6,'Lesha Tolmosov',2013,30,9,12,'winner',9.1),
# (7,'Tima Telegin',2013,6,7.5,10,'winner',9.1),
# (8,'Vitalik Teleyovich',2012,2,11,6.9,'winner',9.1),
# (9,'Lesha OLadyska',2013,10,11,10.2,'winner',9.1),
# (10,'Zakhar Zakharchenko',2012,12,9,9.8,'winner',9.1);
# """)
connection.commit()
def add():
    id=int(input("id:"))
    full_name=(input("full_name:"))
    birth_year=int(input("birth_year:"))
    shoots=int(input("shoots:"))
    avg_score_in_school=float(input("avg_score(school):"))
    avg_score_in_basketball=float(input("avg_score(basketball):"))
    cursor.execute(f"""INSERT INTO basketbolysti 
                            (id, full_name, birth_year,shoots, avg_score_in_school,avg_score_in_basketball) VALUES
                            ({id},'{full_name}',{birth_year}, {shoots},{avg_score_in_school},{avg_score_in_basketball});""")
    connection.commit()
def show_all():
    cursor.execute(f"SELECT * FROM basketbolysti;")
    connection.commit()
    basketbolysti = cursor.fetchall()
    for basketbolyst in basketbolysti:
        print(basketbolyst)
def delete():
    id=int(input("id:"))
    cursor.execute(f"DELETE FROM basketbolysti where id={id}")
    connection.commit()
balance=1000
def ставка_на_команду():
    global balance
    cursor.execute(f"SELECT * FROM basketbolysti;")
    print("WARNING⚠️⚠️⚠️⚠️⚠️⚠️⚠️Don't do big СТАВКА")
    amount = int(input("How much money?"))
    if amount <= balance:
        print(f"Ставка {amount}$   виповнена.")
        balance -= amount
        print(f" баланс: {balance}$")
    else:
        print(f"Нема грошей. Ваш Баланс: {balance}$. Ідіть гуляйте!😂.")

def ставка():
    global balance
    cursor.execute(f"SELECT * FROM basketbolysti;")
    player=(input("What player?"))
    print("WARNING⚠️⚠️⚠️⚠️⚠️⚠️⚠️Don't do big СТАВКА")
    amount=int(input("How much money?"))

    if amount <= balance:
        print(f"Ставка {amount}$ на {player} виповнена.")
        balance -= amount
        print(f" баланс: {balance}$")
    else:
        print(f"Нема грошей. Ваш Баланс: {balance}$. Ідіть гуляйте!😂.")
def подивитися_гру():
    global balance
    cursor.execute(f"SELECT * FROM basketbolysti;")
    balance -= 5
    print(Fore.CYAN)
    print('game:Kyiv_Basket vs Chercasky_mavpy')
    print(Fore.RED)
    print('Рахунок:')
    score_1=random.randint(1, 100)
    score_2=random.randint(1, 100)
    print(f'{score_1} : {score_2}')
    if score_1>score_2:
        print('Win Kyiv Basket')
    else:
        print('Win Chercasky_mavpy')
    print(Fore.WHITE)
def подивитися_результат_ставки():
    print(Fore.LIGHTMAGENTA_EX)
    print('Людина ви по перших платите віртуальною валютою,а по друге ви дитина то робите ставку це дуже погано тому ви все одно програли!😂')
    print(Fore.WHITE)




def menu():
    print("::::FBY::::")
    print("1) add new")
    print("2) show all")
    print("3) delete")
    print("4) ставка")
    print("5) ставка на команду")
    print("6) подивитися гру")
    print("7) подивитися результат ставки")
    print("8) exit")
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
        ставка()
    elif choose=="5":
        ставка_на_команду()
    elif choose=="6":
        подивитися_гру()
    elif choose=="7":
        подивитися_результат_ставки()
    elif choose=="8":
        break
    else:
        print("wrong choice!!!!!!!")
connection.close()



