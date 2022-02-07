from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    "owner": "data-engineering",
    "start_date": datetime(2022, 1, 1),
    "email": ["israelb@sauter.digital"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

dag = DAG(
    "teste-fail",
    default_args=default_args,
    schedule_interval="*/2 * * * *",
    catchup=False,
)


def hello_world():
    print("hello_world")


task_fail = PythonOperator(
    task_id="task_fail", python_callable=hello_world, dag=dag
)
