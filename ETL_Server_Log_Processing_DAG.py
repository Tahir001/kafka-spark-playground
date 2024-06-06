# IMport statements
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'your_name_here',
    'start_date': days_ago(0),
    'email': ['your_email_here'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': True,
}
# Define the ETL dag
etl_dag = DAG(
    dag_id= 'server-processing-logs-dag',
    default_args = default_args,
    description = 'Access server logs from a url endpoint, extract, transform and load them',
    schedule_interval=timedelta(days=1),
)
curl_command = "curl -o https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt web-server-access-log.txt"

task1 = BashOperator(
    task_id = 'download-data',
    bash_command = 'echo \Greetings. This is the second task, transformation.',
    dag=dag,
)



"""
# TASK: CREATE A ETL_Server_Access_Log_Processing DAG! 

Write a DAG named ETL_Server_Access_Log_Processing.py.

    Create the imports block.
    Create the DAG Arguments block. You can use the default settings
    Create the DAG definition block. The DAG should run daily.
    Create the download task. The download task must download the server access log file which is available at the URL:

    1

    curl -o https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt web-server-access-log.txt

    Create the extract task.

    The server access log file contains these fields.

    a. timestamp - TIMESTAMP
    b. latitude - float
    c. longitude - float
    d. visitorid - char(37)
    e. accessed_from_mobile - boolean
    f. browser_code - int

    The extract task must extract the fields timestamp and visitorid.

    Create the transform task. The transform task must capitalize the visitorid.

    Create the load task. The load task must compress the extracted and transformed data.

    Create the task pipeline block. The pipeline block should schedule the task in the order listed below:
        download
        extract
        transform
        load

    Submit the DAG.

    Verify if the DAG is submitted

"""