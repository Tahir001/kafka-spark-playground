# Airflow DAGs has 5 logical blocks
# Library imports
# DAG Arguments
# DAG Definition -> What is the DAG?
# Task Definition - Individual Task Defintions
# Task Pipeline -> Flow of the tasks

# Create a simple pipeline that prints the greeting, and the current date and time
# Repeat it every 5 seconds


from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

import datetime as dt

# Define the default DAG args -- Kind of like settings for a DAG
default_args = {
    'owner': 'Tahir',
    'start_date': days_ago(0),
    'email': ['Tahir.muhammad@mail.utoronto.ca'],
    'retries': 2,
    'retry_delay': dt.timedelta(minutes=5)
}

# DAG Definition -> Instantiate your worflow as a DAG object
dag = DAG(
    'my-first-dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(minutes=1),
)

task1 = BashOperator(
    task_id = 'extract',
    bash_command = 'echo \Greetings. This is the first task, extraction. ',
    dag = dag,
)

task2 = BashOperator(
    task_id = 'transform',
    bash_command = 'echo \Greetings. This is the second task, transformation.',
    dag=dag,
)

task3 = BashOperator(
    task_id = 'load',
    bash_command = 'echo \Greetings. This is the third task, load.',
    dag=dag,
)

task1 >> task2 >> task3
