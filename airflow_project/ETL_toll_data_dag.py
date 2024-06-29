from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

from datetime import timedelta
from process import extract_data


# Define the arguments 
import ETL_project.process as process
#defining DAG arguments
def_args = {
    'owner':'Tahir Muhammad',
    'start_date': 'today',
    'email': ['Tahirm1213@gmail.com'],
    'retries': 	1,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email_on_retry': True,
}

# Define the DAG
etl_toll_dag = DAG(
    "ETL_toll_data",
    default_args=def_args, 
    schedule = "@daily",
    description = "Apache Airflow Final Assignment"
)

# define tasks -- Task 0: Get data 
task0 = BashOperator(
    task_id='download-data',
    bash_command = 
    """
    cd data
    wget 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz'
    echo " Unzip the data"
    tar -xzvf tolldata.tgz -C .
    cd ..
    """,
    dag=etl_toll_dag
) 

# Task 1: Extract data from csv, tsv, and txt file 
task1 = PythonOperator(
    task_id='extract_data_from_all_files',
    python_callable=extract_data,  # Call the extract_data function
    provide_context=True,  # Optional, allows passing context to the function
    dag=etl_toll_dag
)

task2 = BashOperator(
    task_id='consolidate_all_files',
    bash_command = "paste data/transformed/csv_data.csv data/transformed/tsv_data.csv data/transformed/fixed_width_data.csv  > data/final/full_data.csv",
    dag=etl_toll_dag
) 

task0 >> task1 >> task2 >> task3 