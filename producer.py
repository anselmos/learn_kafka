from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    # 'quickstart',
    # group_id='my-group',
    bootstrap_servers=['localhost:9092'],
    retries=5

)

# Asynchronous by default
for _ in range(100):
    producer.send('quickstart', b'raw_bytes')

producer.flush()

future = producer.send('quickstart', key=b'foo', value=b'bar')
# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass
