import sqlite3

import cursor

# Подключаемся к базе данных
#conn = sqlite3.connect(r'C:\Users\Алекс\Documents\GitHub\autoWeb\instance\site.db')
#cursor = conn.cursor()

# Выполняем SQL-запрос
#cursor.execute("SELECT * FROM your_table_name")
#rows = cursor.fetchall()

# Выводим данные
#for row in rows:
#    print(row)

# Закрываем соединение
#conn.close()



#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#tables = cursor.fetchall()
#print("Существующие таблицы:", tables)




#import sqlite3

# Подключаемся к базе данных
#conn = sqlite3.connect(r'C:\Users\Алекс\Documents\GitHub\autoWeb\instance\site.db')
#cursor = conn.cursor()  # Создаем курсор, он должен быть объектом conn.cursor()

# Получаем список таблиц в базе данных
#ursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#tables = cursor.fetchall()
#print("Существующие таблицы:", tables)

# Закрываем соединение
#conn.close()


import sqlite3

# Подключаемся к базе данных
#conn = sqlite3.connect(r'C:\Users\Алекс\Documents\GitHub\autoWeb\instance\site.db')
#cursor = conn.cursor()

# Выполняем SQL-запрос для получения данных из таблицы user
#cursor.execute("SELECT * FROM user")
#rows = cursor.fetchall()

# Выводим данные
#print("Содержимое таблицы 'user':")
#for row in rows:
#    print(row)

# Закрываем соединение
#conn.close()




import sqlite3
from tabulate import tabulate

# Подключаемся к базе данных
conn = sqlite3.connect(r'C:\Users\Алекс\Documents\GitHub\autoWeb\instance\site.db')
cursor = conn.cursor()

# Выполняем SQL-запрос для получения данных из таблицы user
cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()

# Задаём заголовки для таблицы (если известны)
headers = ["ID", "Name", "Email", "Password Hash"]

# Выводим данные в виде таблицы
print("Содержимое таблицы 'user':")
print(tabulate(rows, headers=headers, tablefmt="grid"))

# Закрываем соединение
conn.close()