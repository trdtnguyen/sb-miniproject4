# sb-miniproject4
Data Pipeline Mini Project - Event Ticket System Case Study.
Scheduling workflow using Airflow.
Packaging components in Docker container.

## Setup the project
```
$ git clone https://github.com/trdtnguyen/sb-miniproject4.git
$ docker-compose build && docker-compose up
```
* The project includes two main services: The back-end `mysql_db` and the `airflow` for automation query tasks.
* 


## Important notes
* `airflow` should wait for `mysql_db` ready before access to the database. We implemented that idea using `netcat` package int the `Dockerfile`.
* `airflow` and `mysql_db` should share the same `networks` in order to communiate internally.
* Creating database and tables are done once when starting the container. We didn't include creating databases and tables in the workflow in this project.
* DAG workflow consists of three tasks: extract data from the CSV file and two simple query tasks.

```
<Task(PythonOperator): extract_data>
    <Task(PythonOperator): query2>
    <Task(PythonOperator): query1>
```

## Install and Setup Airflow
### 
```
sudo apt-get update
sudo apt-get install build-essential
pip install \
 apache-airflow==1.10.12 \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.7.txt"
```

## Testing
```
$ airflow list_tasks ticket_event --tree
```
Result:
```
<Task(PythonOperator): extract_data>
    <Task(PythonOperator): query2>
    <Task(PythonOperator): query1>
```
