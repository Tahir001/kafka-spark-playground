from kafka.admin import KafkaAdminClient,NewTopic

# Create a new client 
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# Create a new topic called bankbranch
topic_list = []
new_topic = NewTopic(name="bankbranch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)

admin_client.create_topics(new_topics=topic_list)