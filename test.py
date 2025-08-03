import pandas
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/csv_database")
data=pandas.read_csv('raw_transactions.csv')
transaction=data['transaction_id'].tolist()
amount=data['amount'].tolist()
transaction_data=data['transaction_date'].tolist()
transaction_dict = {
    'transaction_id': transaction,
    'amount': amount,
    'transaction_date': transaction_data
}
transaction_df=pandas.DataFrame(transaction_dict)
customer_name=data['customer_name']
customer_email=data['customer_email']
customer_dict={'customer_name':customer_name,
               'customer_email':customer_email
               }
customer_df=pandas.DataFrame(customer_dict)

product_name=data['product_name']
product_category=data['product_category']
product_data={'product_name':product_name,
              'product_category':product_category}
product_df=pandas.DataFrame(product_data)

customer_df.to_sql('customer_data',engine)
transaction_df.to_sql('transaction_data',engine)
product_df.to_sql('product_data',engine)