"""
Работа с запросами
------------------
Краткое содержание
- Методы записи запросов
- Основы SQL-запросов
- Использование псевдонима
- Сортировка данных по алфавиту
- Ограничение выборки данных
________________________________



"""

import sqlite3

connection = sqlite3.connect("Car_Database.db")

try:
    with connection.cursor() as cursor:
        cursor.execute("""SELECT 
        first_name, last_name, email FROM Customers;""")
except Exception as e:
    print(e)



