from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime
from datetime import timedelta

from ticketevent import ticketevent_main as te

def print_hello():
    print('Hello world!')

WORKFLOW_DAG_ID = 'ticket_event'
WORKFLOW_START_DATE = datetime.now() - timedelta(days=1)
#using CRON format: minutes hours days months dayofweek
#WORKFLOW_SCHEDULE_INTERVAL = '@once'
WORKFLOW_SCHEDULE_INTERVAL = None

WORKFLOW_DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": WORKFLOW_START_DATE,
    "email": ["sb@miniproject.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

#inverval order: minute hour day month day_of_week
dag = DAG(
    WORKFLOW_DAG_ID,
    description="Data pipeline mini-project for ticket event",
    #schedule_interval="0 12 * * *",
    schedule_interval=WORKFLOW_SCHEDULE_INTERVAL,
    default_args=WORKFLOW_DEFAULT_ARGS,
    catchup=False,
)


t1 = PythonOperator(
        task_id='extract_data',
        python_callable=te.run_load_third_party,
        op_kwargs={'file_path_csv': 'db/ticket_sale.csv'},
        dag=dag,
)
t2 = PythonOperator(
        task_id='query1',
        python_callable=te.run_query_best_selling_event,
        dag=dag,
)
t3 = PythonOperator(
        task_id='query2',
        python_callable=te.run_query_best_price_ticket,
        dag=dag,
)

t1 >> [t2, t3]
