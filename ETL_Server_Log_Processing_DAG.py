# IMport statements
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Tahir',
    'start_date': days_ago(0),
    'email': ['Tahir.muhammad@mail.utoronto.ca'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': True,
}

# Define the ETL dag
etl_dag= DAG(
    dag_id='server-processing-logs-dag',
    default_args = default_args,
    description = 'Access server logs from a url endpoint, extract, transform and load them',
    schedule_interval=timedelta(days=1),
)

# Define the tasks
# TASK 1 - Download data 
# Define the tasks
# TASK 1 - Download data 
download_task = BashOperator(
    task_id='download_data',
    bash_command=
    """
    wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%2 scripting/web-server-access-log.txt.gz'
    gunzip -f web-server-access-log.txt.gz
    echo "Extracting data"
    # Extract the columns 1 (timestamp), 2 (latitude), 3 (longitude) and 4 (visitorid)
    cut -d"#" -f1-4 web-server-access-log.txt > extracted-data.txt
    """,
    dag=etl_dag,
)


# Task #2 
transform_task = BashOperator(
    task_id = "transform_data",
    bash_command="python3 /Users/tahir/Desktop/Github/playground_dataeng/transform_data.py",
    dag=etl_dag,
)

download_task >> transform_task