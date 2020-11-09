FROM python:3.7
RUN apt-get update && apt-get -y install build-essential mysql-client
RUN pip install  apache-airflow[mysql,crypto]==1.10.12 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.7.txt"
RUN pip install  mysql-connector-python
RUN pip install  pandas

WORKDIR /root/airflow/
COPY airflow-engine/airflow.sh /root/airflow/airflow.sh
RUN chmod +x airflow.sh

COPY setup.sh /root/airflow/setup.sh
RUN chmod +x setup.sh

COPY airflow-engine/fernet.py /root/airflow/fernet.py
COPY airflow-engine/mysqlconnect.py /root/airflow/mysqlconnect.py
COPY airflow-engine/dags /root/airflow/
COPY ticketevent /root/airflow/ 
COPY sql /root/airflow/
COPY db /root/airflow/

CMD ./setup.sh

CMD ./airflow.sh
