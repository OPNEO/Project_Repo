import random
import pandas
import os
from time import sleep
from datetime import datetime

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM STUDENT')

# csv_file_path = 'csv_data/weather_data.csv'
# file_exists = os.path.exists(csv_file_path)
# for x in range(5):
#     temperature=random.randint(0,50)
#     humidity=random.randint(0,50)
#     pressure=random.randint(0,50)
#     temperature=temperature
#     timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     data={'temperature':[temperature],
#         'humidity':[humidity],
#         'pressure':[pressure],
#         'timestamp': [timestamp],
#         }
#     print('New_Records',data)
#     df = pandas.DataFrame(data)
#
#     df.to_csv(csv_file_path, mode='a', header=not file_exists, index=False)
#
#     file_exists = True
#
#     sleep(1)