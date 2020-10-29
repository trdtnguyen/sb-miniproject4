import mysql.connector
import pandas as pd
from numpy import record


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='root',
                                             password='12345678',
                                             host='localhost',
                                             port='3306',
                                             database='ticket_event')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)

    return connection


def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()
    df = pd.read_csv(file_path_csv)
    st = ("INSERT INTO ticket_sale "
          "(ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, event_addr, customer_id, price, num_tickets) "
          " VALUES (%(ticket_id)s, %(trans_date)s, %(event_id)s,"
          " %(event_name)s, %(event_date)s, %(event_type)s, %(event_city)s, %(event_addr)s,"
          " %(customer_id)s, %(price)s, %(num_tickets)s)")
    print(st)
    try:
        for i, row in df.iterrows():
            insert_val = {}
            insert_val['ticket_id'] = int(row['ticket_id'])
            insert_val['trans_date'] = int(row['trans_date'])
            insert_val['event_id'] = int(row['event_id'])
            insert_val['event_name'] = row['event_name']
            insert_val['event_date'] = row['event_date']
            insert_val['event_type'] = row['event_type']
            insert_val['event_city'] = row['event_city']
            insert_val['event_addr'] = row['event_addr']
            insert_val['customer_id'] = int(row['customer_id'])
            insert_val['price'] = float(row['price'])
            insert_val['num_tickets'] = int(row['num_tickets'])

            cursor.execute(st, insert_val)
    except Exception as e:
        print(e)
    # [Iterate through the CSV file and execute insert statement]
    connection.commit()
    cursor.close()


def query_best_selling_event(connection):
    # Get the best selling event in the past month
    sql_statement = ("SELECT event_name, SUM(num_tickets) "
                     "FROM ticket_sale "
                     "GROUP BY event_name "
                     "ORDER BY SUM(num_tickets) DESC "
                     "LIMIT 1")
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

def print_best_selling_event(records):
    print("Best selling events:")
    for record in records:
        print(f' - {record[0]}: number sold ticket {record[1]}')

def query_best_price_ticket(connection):
    # Get the best price event in the past month
    sql_statement = ("SELECT ticket_id, event_name, event_date, price "
                     "FROM ticket_sale "
                     "ORDER BY price DESC "
                     "LIMIT 1")

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

def print_best_price_ticket(records):
    print("Best price ticket:")
    for record in records:
        print(f' - {record[0]}: at event {record[1]} on {record[2]} with price: {record[3]}')

file_path_csv = 'ticket_sale.csv'
connection = get_db_connection()
#load_third_party(connection, file_path_csv)
records = query_best_selling_event(connection)
print_best_selling_event(records)

records = query_best_price_ticket(connection)
print_best_price_ticket(records)


connection.close()