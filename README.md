# Big Data Engineering Playground

The following repo is a playground for me to learn and mess around with big data tools such as Apache Airflow, Kafka, Spark, and Hadoop.

# kafka-aiflow-playground
A small pet project to play around with Kafka and Airflow. 
Some notes on the topic can be found here: https://tahirm.notion.site/Apache-Kafka-5579b28738ab423db41891dfaae8b682?pvs=4

# Technical Requirements 
You will need: Python3, Postgres, Airflow, Docker, Docker-compose, Kafka, Kafka-python and Zookeeper.

# Details - Kafka
The following project uses Zookeeper to manage a Kafka Cluster to create a new topic called Toll Plaza which keeps track of incoming cars at different Plazas.

We use a Kafka producer to produce incoming traffic, a consumer to read the traffic, and post relevent information into a Postgres Database. 

# Documentation for reproducing the results:

1. Start postgres and run the create_db.sql command to create a newdatabse called 'tolldata', and create a table 'livetolldata' inside of it.

2. Run the `docker-compose up` command in the project directory to run the Zookeeper and Kafkaserver on a connected dockerized network
   
3. Create a new topic called toll:
   `docker exec -it mykafkaserver /opt/kafka/bin/kafka-topics.sh --create --topic toll --bootstrap-server localhost:9092`
   
4. Run the toll traffic generator by `python3 toll_traffic_generator.py` to start producing live toll traffic feed.
![Screenshot 2024-06-15 at 4 52 01 PM](https://github.com/Tahir001/kafka-airflow-playground/assets/51174301/abd50c48-0c7c-4dee-bb78-90981775cc97)

5. Run the toll traffic consumer by `python3 streaming_data_reader.py` to start consuming live toll traffic feed and ingest it into the Postgres DB.
![Screenshot 2024-06-15 at 4 53 44 PM](https://github.com/Tahir001/kafka-airflow-playground/assets/51174301/0be426d3-4c65-4740-8b0c-b7ff83978b9e)

6. Then we can connect to our postgres and see the data is actually there:
<img width="512" alt="Screenshot 2024-06-15 at 4 59 18 PM" src="https://github.com/Tahir001/kafka-airflow-playground/assets/51174301/eecf3f69-d8e7-48ea-855e-e5f1993268f8">
