INIT_FILE=.airflowinitialized
if [ ! -f $INIT_FILE ]; then
    # Create all Airflow configuration files
    #airflow initdb
    #rm /root/airflow/airflow.db

    # Secure the storage of connections’ passwords
    #python fernet.py

    # Wait until the DB is ready
    apt update && apt install -y netcat
    echo "wait mysql on 3306 to open ..."
    while ! nc -z mysql_db 3306; do
        sleep 10
    done
    apt remove -y netcat

    # Setup the DB for airflow
    #python mysqlconnect.py
    airflow initdb

    # Setup app DB
    python ticketevent/setup_db.py
    # This configuration is done only the first time
    touch $INIT_FILE
fi

# Run the Airflow webserver and scheduler
#airflow scheduler &
#airflow webserver &
wait
