import json
from kafka import KafkaProducer

# Start a producer
# The producer is responsible for sending messages to the Kafka topic.
# We configure it to serialize message values as JSON.
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Send data to the bankbranch topic 
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})
producer.send("bankbranch", {'atmid':1, 'transid':102})
producer.send("bankbranch", {'atmid':2, 'transid':103})
producer.send("bankbranch", {'atmid':1, 'transid':104})
producer.send("bankbranch", {'atmid':2, 'transid':105})

producer.flush()

producer.close()