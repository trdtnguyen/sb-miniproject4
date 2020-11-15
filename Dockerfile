FROM python:3.7
RUN apt-get update && apt-get -y install build-essential
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
COPY airflow-engine/dags /root/airflow/dags

COPY ticketevent /root/airflow/ticketevent
COPY sql /root/airflow/sql
COPY db /root/airflow/db

#wait for mysql ready
#ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
#RUN chmod +x /wait
#CMD /wait && npm start
#RUN sleep 5

#CMD ./setup.sh

#CMD ./airflow.sh
