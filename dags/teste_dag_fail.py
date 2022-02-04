from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.exceptions import AirflowFailException



default_args = {
    "owner": "data-engineering",
    "start_date": datetime(2022, 1, 1),
    "email": ["israelb@sauter.digital"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10)
}

dag = DAG("teste-dag-fail", default_args=default_args, schedule_interval="*/2 * * * *", catchup=False)


def hello_world():
    print("Hello-world!")


print_hello = PythonOperator(task_id="print_hello", python_callable=hello_world, dag=dag)
print_hello = PythonOperator(task_id="print_hello", python_callable=hello_world, dag=dag)


