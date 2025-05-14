# airflowSparkPOC
Simple end to end working app using apache airflow and apache spark POC

1. Setup & Basic Pipelines
   Spin up an Airflow environment using docker compose - Local for now
2. cd airflow
3. Check the following : directory airflow - dags - 2 dag file, please read them before you run them
4. Check the directory spark - scripts - 1 spark script to be run on spark cluster
5. Do cd airflow 
6. Execute docker compose up -d 
7. Check all containers up and running in healthy state
8. cd apache-spark
9. docker compose up -d
10. Check 2 spark containers running

# UI details
1. localhost:8080 - airflow ( airflow/airflow)
2. localhost:8081 - spark

# How to execute dag
The docker compose would pick the dag py file from shared folder and add that to /opt/airflow/dags directory
check in airflow.cfg config frequency to run the file, Dag should be automatically picked up and would be visible to run in UI
The files currently dont run automatically, trigger them

1. firstWorkflow.py would run a simple aiflow task, needs to be triiggered manually
2. sparkWorkflow.py would execute task on a spark cluster, check the file it uses to run spark job

