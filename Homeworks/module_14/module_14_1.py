import sqlite3


connection = sqlite3.connect("Homeworks/module_14/not_telegram.db")
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )"""
)


for i in range(1, 11):
    cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (f"User{i}", f"example{i}@gmail.com", int(f"{i}0"), 1000),
    )

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))

cursor.execute("DELETE FROM Users WHERE (id - 1) % 3 = 0")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT username, email, age, balance FROM Users")

users = cursor.fetchall()

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

# cursor.execute("SELECT AVG(balance) FROM Users")
# avg_balanse = cursor.fetchone()[0]
# print(avg_balanse)


# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.commit()
connection.close()
