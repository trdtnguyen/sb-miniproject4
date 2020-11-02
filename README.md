# sb-miniproject4
Data Pipeline Mini Project - Event Ticket System Case Study

## Install and Setup Airflow
### 
```
sudo apt-get update
sudo apt-get install build-essential
pip install \
 apache-airflow==1.10.12 \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.7.txt"
```

### Install required packages
```
pip install mysql-connector-python
pip install pandas
```
### Init Database
This project using MySQL 8.0 as the backend database.

MySQL installation guide for [Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html) and [Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html). 

* ***Create Database:*** Create a database named `ticket_event`
```
$ mysqladmin -u root -p create ticket_event
```
* ***Create tables:*** To create tables in `ticket_event` database:
```
$ mysql -u root -p ticket_event < sql/create_table.sql
``` 
### Init Airflow's database
Inside the working directory that you clone from git, init the local database used by Airflow
```
$ airflow initdb
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
