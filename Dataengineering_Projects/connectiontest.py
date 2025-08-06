import psycopg2
conn=psycopg2.connect(dbname='CSV_DATA',user='postgres',password=1234,port=5432,host='localhost')
cursor=conn.cursor()
cursor.execute('SELECT * FROM customer_dat')