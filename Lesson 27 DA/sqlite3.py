import sqlite3
connection = sqlite3.connect("data.db")

sql = connection.cursor()
users = sql.execute("SELECT * FROM user;").fetchall()

connection2 = sqlite3.connect("data2.db")
sql2 = connection2.cursor()
sql2.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER, user_name TEXT, phone_number TEXT, language TEXT);")
connection2.commit()
for user in users:
    sql2.execute(f"INSERT INTO user (id, user_name, phone_number, language) VALUES (?, ?, ?, ?);", (user[0]+1, user[2], user[3], user[4]))
connection2.commit()
print(users)
