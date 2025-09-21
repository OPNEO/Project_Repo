from kafka import KafkaProducer
from json import dumps
import psycopg2
import datetime

# PostgreSQL connection
con = psycopg2.connect(
    user='postgres',
    password='1234',
    host='localhost',
    port=5432,
    dbname='dvdrental'
)
cursor = con.cursor()
cursor.execute('SELECT * FROM customer')
rows = cursor.fetchall()

colnames = [desc[0] for desc in cursor.description]

# Kafka Confluent Cloud configs
BOOTSTRAP_SERVERS = "pkc-921jm.us-east-2.aws.confluent.cloud:9092"
API_KEY = "SPQMH4XEBTMYQIQB"
API_SECRET = "cfltxNgD84v6uvlZTEl1siNK3nE3CXBDEp6r4BNnTYE4CZohyD2E+YG62V/6+GeQ"

# ✅ JSON serializer for non-serializable types
def json_serializer(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_plain_username=API_KEY,
    sasl_plain_password=API_SECRET,
    client_id="python-producer",
    key_serializer=lambda k: str(k).encode("utf-8"),   # customer_id as key
    value_serializer=lambda v: dumps(v, default=json_serializer).encode("utf-8")
)

# ✅ Send rows to Kafka
for row in rows:
    record = {col: val for col, val in zip(colnames, row)}
    customer_id = record["customer_id"]
    producer.send("customer_data", key=customer_id, value=record)
    print(f"Sent -> Key: {customer_id}, Value: {record}")

producer.flush()
print("✅ All records sent successfully with customer_id as key!")
