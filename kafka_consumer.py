from kafka import KafkaConsumer

# Create a Kafka consumer
# The consumer is responsible for reading messages from the Kafka topic.
# We configure it to read from the 'bankbranch' topic, deserialize JSON messages, and start reading from the beginning of the topic.
consumer = KafkaConsumer('bankbranch',
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')
print("Hello")
print(consumer)


# Get messages from the consumer
# This loop reads and prints messages from the 'bankbranch' topic.
# It will run indefinitely until stopped manually.
for msg in consumer:
    print(msg.value.decode("utf-8"))