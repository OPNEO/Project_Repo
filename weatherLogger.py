import random
from time import sleep
from datetime import datetime
import sqlite3
try:
    conn=sqlite3.connect('csv_data.db')
    cursor=conn.cursor()
    query = "INSERT INTO temperature VALUES(?, ?, ?, ?)"
    for x in range(100):
        temperature=random.randint(0,50)
        humidity=random.randint(0,50)
        pressure=random.randint(0,50)
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query,(temperature, humidity, pressure, timestamp))
        conn.commit()
        print('inserted and Commited')
        sleep(0.2)
except Exception as e:
    print(e)
finally:
    print('Completed Execution ')