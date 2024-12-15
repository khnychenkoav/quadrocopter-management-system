import unittest
from unittest.mock import patch, MagicMock
from src.utils.kafka_producer_wrapper import KafkaProducerWrapper

class TestKafkaProducerWrapper(unittest.TestCase):
    @patch('src.utils.kafka_producer_wrapper.KafkaProducer')
    def test_send_message(self, MockKafkaProducer):
        # Настройка мока
        mock_producer = MockKafkaProducer.return_value
        mock_future = MagicMock()
        mock_producer.send.return_value = mock_future
        mock_future.get.return_value = MagicMock(topic='test_topic', partition=0, offset=0)

        # Создание экземпляра KafkaProducerWrapper
        producer_wrapper = KafkaProducerWrapper(bootstrap_servers=['localhost:9092'], topic='test_topic')

        # Отправка сообщения
        message = {'key': 'value'}
        producer_wrapper.send_message(message)

        # Проверка вызовов
        mock_producer.send.assert_called_once_with('test_topic', message)
        mock_future.get.assert_called_once_with(timeout=10)

    @patch('src.utils.kafka_producer_wrapper.KafkaProducer')
    def test_close(self, MockKafkaProducer):
        # Настройка мока
        mock_producer = MockKafkaProducer.return_value

        # Создание экземпляра KafkaProducerWrapper
        producer_wrapper = KafkaProducerWrapper(bootstrap_servers=['localhost:9092'], topic='test_topic')

        # Закрытие продюсера
        producer_wrapper.close()

        # Проверка вызовов
        mock_producer.flush.assert_called_once()
        mock_producer.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()