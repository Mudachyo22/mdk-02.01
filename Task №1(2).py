import sqlite3 as sql
import os

def create_db(name):
    if name:
        db_path = f"{name}.db"
        if not os.path.exists(db_path):
            with sql.connect(db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS datelist (
                        name TEXT,
                        city TEXT,
                        age INTEGER
                    )
                """)
            print(f"База данных '{name}' успешно создана! Поля для ввода: Имя, Город и Возраст.")
        else:
            print(f"Ошибка: база данных с именем '{name}' уже существует.")
    else:
        print("Ошибка: введите название новой базы данных.")

def add_date(name, value_name, value_city, value_age):
    db_path = f"{name}.db"
    with sql.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO datelist (name, city, age) VALUES (?, ?, ?)", 
                       (value_name, value_city, value_age))

def get_date(name):
    db_path = f"{name}.db"
    with sql.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM datelist")
        user_data = cursor.fetchall()
        print(user_data)

def main():
    while True:
        try:
            num = int(input("\nВведите номер команды:\n"
                            "1. Создать новую базу данных\n"
                            "2. Прочитать базу данных\n"
                            "3. Добавить значения в базу данных\n"
                            "0. Для выхода из программы\n"
                            "Ваш выбор: "))
        except ValueError:
            print("Ошибка: Введите только номер команды!")
            continue
        
        if num == 0:
            print("Вы завершили работу с программой.")
            break
        elif num == 1:
            name = input("Введите название новой базы данных (без .db): ")
            create_db(name)
        elif num == 2:
            name = input("Введите название базы данных для чтения (без .db): ")
            get_date(name)
        elif num == 3:
            name = input("Введите название базы данных для добавления значений (без .db): ")
            value_name = input("Введите имя: ")
            value_city = input("Введите город: ")
            try:
                value_age = int(input("Введите возраст: "))
            except ValueError:
                print("Ошибка: Введите корректный возраст.")
                continue
            add_date(name, value_name, value_city, value_age)
        else:
            print("Ошибка: Неверный номер команды. Попробуйте снова.")


main()