import random
import time
import json
import yaml
import pycountry
import logging
from kafka import KafkaProducer
from datetime import datetime
import uuid

# Set up logging
logging.basicConfig(
    filename='transaction_producer.log',  # Log file name
    filemode='a',  # Append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Log level
)

# Load Kafka configuration from the YAML file
def load_config():
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)
        kafka_broker = config['kafka']['broker'] 
        kafka_topic = config['kafka']['topic']
        tx_interval = config['tx_interval'] 
    return kafka_broker, kafka_topic, tx_interval

# List of possible values for certain fields
transaction_status = ['Pending', 'Completed', 'Failed', 'Refunded', 'Cancelled']
transaction_type = ['Purchase', 'Refund', 'Chargeback', 'Payment', 'Transfer']
payment_gateway = ['Visa', 'Master', 'Stripe', 'PayPal', 'X Digital Bank', 'Y Commercial Bank']
payment_status = ['Authorized', 'Captured', 'Settled', 'Failed', 'Voided']
transaction_source = ['Mobile App', 'Web App', 'In-store', 'API', 'Other']


# Function to generate random country names for src/dest transaction location
def random_country():
    countries = [country.name for country in pycountry.countries]
    return random.choice(countries)

# Function to generate a unique transaction ID
def generate_transaction_id():
    timestamp = int(time.time() * 1000)
    random_component = random.randint(1000, 9999)  # A random number to add uniqueness
    transaction_id = f"{timestamp}-{random_component}" # Construct the transaction ID in the format: <timestamp>-<random_component>
    return transaction_id


# Function to generate random transaction
def generate_transaction():
    transaction = {
        "transaction_id": generate_transaction_id(),
        "user_id": random.randint(1, 50),
        "merchant_id": random.randint(1, 30),
        "payment_method_id": random.randint(1, 10),
        "amount": round(random.uniform(5.0, 5000.0), 2),
        "currency": 'USD',
        "transaction_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "status": random.choice(transaction_status),
        "transaction_type": random.choice(transaction_type),
        "payment_gateway": random.choice(payment_gateway),
        "payment_status": random.choice(payment_status),
        "src_transaction_location": random_country(),
        "dest_transaction_location": random_country(),
        "transaction_source": random.choice(transaction_source)
    }
    return transaction

# Callback function to handle delivery reports
def on_send_success(record_metadata):
    success_msg = f"Message successfully sent to topic: {record_metadata.topic}, "f"partition: {record_metadata.partition}, "f"offset: {record_metadata.offset}"
    logging.info(success_msg)
    print(success_msg+"\n")

def on_send_error(excp):
    error_msg = f"Message delivery failed: {excp}"
    logging.info(error_msg)
    print(error_msg+"\n")

# Load configuration data
kafka_broker, kafka_topic, tx_interval = load_config()

# Create Kafka producer
kafka_producer = KafkaProducer(bootstrap_servers=kafka_broker, retries=5)

# Infinite loop to generate and send transaction every second
while True:
    transaction = generate_transaction()
    try:
        future = kafka_producer.send(kafka_topic, value=json.dumps(transaction).encode('utf-8'))
        future.add_callback(on_send_success)
        future.add_errback(on_send_error)
        transaction_msg = f"Sent transaction: {transaction}"
        logging.info(transaction_msg)
        print(transaction_msg)
    except Exception as e:
        exception_msg =f"Error while sending message: {e}"
        logging.error(exception_msg)
        print(exception_msg)
    time.sleep(tx_interval)  # Send a new transaction every second
