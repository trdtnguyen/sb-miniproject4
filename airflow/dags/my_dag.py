from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print('Hello world!')

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": "2020-10-20",
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

#inverval order: minute hour day month day_of_week
dag = DAG(
    "hello_world",
    description="Hello world Airflow",
    #schedule_interval="0 12 * * *",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
)

t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag,
)
t2 = PythonOperator(task_id="hello_task", python_callable=print_hello, dag=dag)

t1 >> t2
