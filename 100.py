import sqlite3

# 1. Подключаемся к базе данных (если файла test.db нет, он создастся)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 2. Создаем таблицу users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary INTEGER
)
''')

# 3. Наполняем таблицу данными
users_data = [
    (1, 'user1', 23, 400),
    (2, 'user2', 25, 500),
    (3, 'user3', 23, 500),
    (4, 'user4', 30, 900),
    (5, 'user5', 27, 500),
    (6, 'user6', 28, 900)
]

cursor.executemany('INSERT INTO users VALUES (?, ?, ?, ?)', users_data)

# 4. Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных test.db и таблица users успешно созданы!")