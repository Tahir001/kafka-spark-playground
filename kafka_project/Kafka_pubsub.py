# Full file as an example
import json
from kafka.admin import KafkaAdminClient
from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
from kafka import KafkaProducer 
from kafka import KafkaConsumer

# Create a Kafka Admin client
# This client allows us to create, delete, and manage Kafka topics.
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# Create a topic
# Here, we define a new topic named 'bankbranch' with 2 partitions and a replication factor of 1.
topics_list = []
new_topic = NewTopic(name='bankbranch', num_partitions=2, replication_factor=1)
topics_list.append(new_topic)

# Create the topics on the Kafka broker
# This command sends the topic creation request to the Kafka broker.
admin_client.create_topics(new_topics=topics_list)

# Describe configurations of the Kafka topic
# This retrieves and prints the configurations for the 'bankbranch' topic.
configs = admin_client.describe_configs(config_resources=[ConfigResource(ConfigResourceType.TOPIC, "bankbranch")])
for config in configs:
    print(config)

# Start a producer
# The producer is responsible for sending messages to the Kafka topic.
# We configure it to serialize message values as JSON.
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Send data from the producer
# Here we send three messages to the 'bankbranch' topic.
producer.send("bankbranch", {'atmid': 1, 'transid': 100})
producer.send("bankbranch", {'atmid': 2, 'transid': 101})
producer.send("bankbranch", {'atmid': 1, 'transid': 103})

# Wait for all messages to be sent
# This ensures that all buffered messages are sent to the Kafka broker.
producer.flush()

# Create a Kafka consumer
# The consumer is responsible for reading messages from the Kafka topic.
# We configure it to read from the 'bankbranch' topic, deserialize JSON messages, and start reading from the beginning of the topic.
consumer = KafkaConsumer(
    'bankbranch',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Get messages from the consumer
# This loop reads and prints messages from the 'bankbranch' topic.
# It will run indefinitely until stopped manually.
for msg in consumer:
    print(msg.value)

# Close the admin client and producer
# Properly close the admin client and producer to release resources.
admin_client.close()
producer.close()
