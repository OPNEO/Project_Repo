import psycopg2
conn=psycopg2.connect(dbname='CSV_DATA',user='postgres',password=1234,host='localhost',port=5432)
cursor=conn.cursor()
cursor.execute('create table transactions2 (transaction_id INT PRIMARY KEY ,customer_name TEXT NOT NULL,customer_email VARCHAR NOT NULL,product_name VARCHAR,product_category VARCHAR ,amount INT,transaction_date DATE)')
conn.commit()
cursor.execute("SELECT * FROM transactions")
data=cursor.fetchall()

for x in data:
    data=list(x)
    transaction_id = data[0]
    customer_name = data[1]
    customer_email = data[2]
    product_name = data[3]
    product_category = data[4]
    amount = data[5]
    transaction_date = data[6]
    insert_query = """
          INSERT INTO transactions2 (
              transaction_id, customer_name, customer_email, product_name, 
              product_category, amount, transaction_date
          ) VALUES (%s, %s, %s, %s, %s, %s, %s);
          """

    record_to_insert = (
        transaction_id, customer_name, customer_email, product_name,
        product_category, amount, transaction_date
    )
    cursor.execute(insert_query, record_to_insert)
    conn.commit()
    print(f"Record for transaction_id {transaction_id} inserted successfully.")
