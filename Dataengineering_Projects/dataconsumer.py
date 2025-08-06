import json
from kafka import KafkaConsumer
import psycopg2

# DB_PARAMS = {
#     'host': 'localhost',
#     'database': 'CSV_DATA',
#     'user': 'postgres',
#     'password': 1234,
#     'port':5431
# }

try:
    conn=psycopg2.connect(dbname='CSV_DATA',user='postgres',password=1234,port=5432,host='localhost')
    cursor = conn.cursor()
    print("Database connection established successfully.")

    consumer = KafkaConsumer(
        'csv_data',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='test33',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for msg in consumer:
        data = msg.value

        transaction_id = data.get('transaction_id')
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        product_name = data.get('product_name')
        product_category = data.get('product_category')
        amount = data.get('amount')
        transaction_date = data.get('transaction_date')

        insert_query = """
        INSERT INTO transactions (
            transaction_id, customer_name, customer_email, product_name, 
            product_category, amount, transaction_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        record_to_insert = (
            transaction_id, customer_name, customer_email, product_name,
            product_category, amount, transaction_date
        )

        try:
            cursor.execute(insert_query, record_to_insert)
            conn.commit()
            print(f"Record for transaction_id {transaction_id} inserted successfully.")

        except psycopg2.Error as e:
            print(f"Database error while inserting record: {e}")
            conn.rollback()

except psycopg2.Error as e:
    print(f"Failed to connect to the database: {e}")

finally:
    if 'conn' in locals() and conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")