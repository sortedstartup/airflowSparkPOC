from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 14),
}

# Define the DAG with a unique dag_id
with DAG(
    dag_id='hello_spark',
    description="spark",
    default_args={'owner': 'airflow'},
    schedule=None,
    catchup=False,
) as dag:

    # Configure SparkSubmitOperator
    spark_submit_task = SparkSubmitOperator(
        task_id='spark_submit_task',
        conn_id='spark_default',  # Spark connection ID (optional)
        application='/opt/airflow/sparkWorkflow.py',  # Path to your Spark job
        name='spark-job',
        conf={'spark.master': 'spark://spark-master:7077'},  # Spark master
        driver_memory='2g',
        executor_memory='2g',
        executor_cores=2,
        total_executor_cores=4,
    )