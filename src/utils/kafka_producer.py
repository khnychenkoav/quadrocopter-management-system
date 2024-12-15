from kafka import KafkaProducer
import json

class KafkaProducerWrapper:
    def __init__(self, bootstrap_servers=['localhost:9092'], topic='trajectory_topic'):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic

    def send_message(self, message):
        try:
            future = self.producer.send(self.topic, message)
            record_metadata = future.get(timeout=10)
            print(f"Сообщение отправлено в {record_metadata.topic} раздел {record_metadata.partition} смещение {record_metadata.offset}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")

    def close(self):
        self.producer.flush()
        self.producer.close()
