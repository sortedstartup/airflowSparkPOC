from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

def print_hello():
    print('Hello, Airflow!')

# Use pendulum for the start date
local_tz = pendulum.timezone("UTC")

with DAG(
    dag_id='hello_airflow',
    description="A simple tutorial DAG",
    default_args={'owner': 'airflow'},
    schedule=None,
    start_date=pendulum.now('UTC').subtract(days=1),  # Subtracting one day
    catchup=False,
) as dag:
    task_hello = PythonOperator (
        task_id='print_hello',
        python_callable=print_hello,
    )

    task_hello