from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args ={
    'owner':'airflow',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id="our_first_dag2",
    default_args=default_args,
    description="test",
    start_date=datetime(2023,10,1),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command="echo hello again"
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo hello again 3"
    )

    task1 >> task2
    task1 >> task3