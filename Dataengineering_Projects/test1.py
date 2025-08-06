import csv
import json
from kafka import KafkaProducer
prod=KafkaProducer(bootstrap_servers=['localhost:9092'],
                   value_serializer=lambda x :json.dumps(x).encode('utf-8') )
with open('../raw_transactions.csv') as file:
    data=csv.DictReader(file)
    for x in data:
        prod.send('csv_data',value=x)
