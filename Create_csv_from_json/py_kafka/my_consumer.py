from confluent_kafka import Consumer
import json
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}

def consumer_process():
    consumer = Consumer(consumer_config)
    consumer.subscribe(['my-orders'])
    
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            
            order_data = json.loads(msg.value().decode('utf-8'))
            print(f"Received order: {order_data}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    consumer_process()