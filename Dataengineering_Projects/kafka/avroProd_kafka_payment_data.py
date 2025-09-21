from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer
import psycopg2
import datetime
import decimal


# Avro Schema for "payment" table
schema_str = """
{
  "type": "record",
  "name": "Payment",
  "namespace": "dvdrental",
  "fields": [
    {"name": "payment_id", "type": "int"},
    {"name": "customer_id", "type": "int"},
    {"name": "staff_id", "type": "int"},
    {"name": "rental_id", "type": ["null", "int"], "default": null},
    {"name": "amount", "type": "double"},
    {"name": "payment_date", "type": "string"}
  ]
}
"""

# ✅ Schema Registry client
schema_registry_conf = {
    'url': "https://psrc-q25x7.us-east-2.aws.confluent.cloud",
    'basic.auth.user.info': "3MMCOSYCL7OMNCWG:cfltsDgiR+Uf1vXRWSppytYp/x0V1a2q+36Kp8Iijspc54qllnebRkcbJbZx3GEw"
}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# ✅ Avro serializer
avro_serializer = AvroSerializer(schema_registry_client, schema_str)

# ✅ Kafka Producer config
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


# ✅ PostgreSQL connection
con = psycopg2.connect(
    user='postgres',
    password='1234',
    host='localhost',
    port=5432,
    dbname='dvdrental'
)
cursor = con.cursor()
cursor.execute('SELECT * FROM payment')
rows = cursor.fetchall()
colnames = [desc[0] for desc in cursor.description]


# ✅ Send rows as Avro
for row in rows:
    record = {}
    for col, val in zip(colnames, row):
        if isinstance(val, (datetime.date, datetime.datetime)):
            record[col] = val.isoformat()         # date → string
        elif isinstance(val, decimal.Decimal):
            record[col] = float(val)              # decimal → float
        else:
            record[col] = val

    producer.produce(
        topic="payment_data_avro",
        key=str(record["payment_id"]),
        value=record
    )
    print(f"Sent Avro -> {record}")

producer.flush()
print("✅ All payment records sent successfully in Avro format!")
