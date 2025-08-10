import sqlite3
conn=sqlite3.connect('E:\\water-tanker\\tanker.db')
cursor=conn.cursor()
cursor.execute('SELECT * FROM bookings')
print(cursor.fetchall())
