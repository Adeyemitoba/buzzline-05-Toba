import json
import sqlite3
from kafka import KafkaConsumer
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Configuration variables (should match your .env or config setup)
kafka_topic = 'buzzline_db'
kafka_server = 'localhost:9092'
db_file = 'sentiment_analysis.db'

# Set up the database connection and create a table if not exists
conn = sqlite3.connect(db_file)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS sentiment_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT,
        timestamp TEXT,
        category TEXT,
        sentiment REAL,
        keyword TEXT,
        message_length INTEGER
    )
''')
conn.commit()

# Define the function to insert data into the SQLite database
def insert_data(data):
    with conn:
        c.execute("""
            INSERT INTO sentiment_data (author, timestamp, category, sentiment, keyword, message_length) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (data['author'], data['timestamp'], data['category'], data['sentiment'], data['keyword_mentioned'], data['message_length']))
        conn.commit()

# Initialize Kafka consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=[kafka_server],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Process messages
try:
    for message in consumer:
        print("Received:", message.value)
        insert_data(message.value)
except KeyboardInterrupt:
    print("Interrupted")
finally:
    consumer.close()
    conn.close()

