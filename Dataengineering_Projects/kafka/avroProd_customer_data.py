from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer
import psycopg2
import datetime

schema_str = """
{
  "type": "record",
  "name": "Customer",
  "namespace": "dvdrental",
  "fields": [
    {"name": "customer_id", "type": "int"},
    {"name": "store_id", "type": "int"},
    {"name": "first_name", "type": "string"},
    {"name": "last_name", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "address_id", "type": "int"},
    {"name": "activebool", "type": "boolean"},
    {"name": "create_date", "type": "string"},
    {"name": "last_update", "type": "string"}
  ]
}
"""

# ✅ Schema Registry client
schema_registry_conf = {
    'url': "https://psrc-q25x7.us-east-2.aws.confluent.cloud",
    'basic.auth.user.info': "3MMCOSYCL7OMNCWG:cfltsDgiR+Uf1vXRWSppytYp/x0V1a2q+36Kp8Iijspc54qllnebRkcbJbZx3GEw"
}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

avro_serializer = AvroSerializer(schema_registry_client, schema_str)

producer_conf = {
    'bootstrap.servers': "pkc-921jm.us-east-2.aws.confluent.cloud:9092",
    'security.protocol': "SASL_SSL",
    'sasl.mechanism': "PLAIN",
    'sasl.username': "SPQMH4XEBTMYQIQB",
    'sasl.password': "cfltxNgD84v6uvlZTEl1siNK3nE3CXBDEp6r4BNnTYE4CZohyD2E+YG62V/6+GeQ",
    'key.serializer': StringSerializer('utf_8'),
    'value.serializer': avro_serializer
}

producer = SerializingProducer(producer_conf)

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

for row in rows:
    record = {col: val if not isinstance(val, (datetime.date, datetime.datetime)) else str(val)
              for col, val in zip(colnames, row)}
    producer.produce(topic="customer_data", key=str(record["customer_id"]), value=record)
    print(f"Sent Avro -> {record}")

producer.flush()
print("✅ All records sent successfully in Avro format!")
