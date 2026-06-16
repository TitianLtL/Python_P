import uuid
import json
from confluent_kafka import Producer
    
producer_config ={
    'bootstrap.servers': 'localhost:9092'
    }


def producer_process():
    producer = Producer(producer_config)

    order = {
        'order_id': str(uuid.uuid4()),
        'customer_id': 456,
        'items': [
            {'item_id': 1, 'quantity': 2},
            {'item_id': 2, 'quantity': 1}
        ],
        'total_price': 29.99
    }
    order_json = json.dumps(order).encode('utf-8')
    producer.produce(topic= "my-orders", 
                    value= order_json, 
                    callback=delivery_report 
                    )
    producer.flush()
    
def delivery_report(err, msg):
    if err is not None:
        print(f" Message delivery failed: {err}")
    else:
        print(f"Message {msg.value().decode('utf-8')} delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


if __name__ == "__main__":
    producer_process()