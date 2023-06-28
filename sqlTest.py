# THIS IS JUST TEST RUNS NOTHING SERIOUS YET


import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print('MySQL Database connection successful')
    except Error as err:
        print(f"Error: '{err}'")
    return connection


pw = 'Qsw/>ePBkYXpH1H'
db = 'mysql_python'
connection = create_server_connection('localhost', 'root', pw)


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database created successfully')
    except Error as err:
        print(f"Error:'{err}'")


# create_database_query = "Create database mysql_python"
# create_database(connection, create_database_query)


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("My SQL database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error: '{err}'")

create_orders_table = """
create table orders(
order_id int primary key,
customer_name varchar(30) not null,
product_name varchar(20) not null,
date_ordered date,
quantity int,
unit_price float,
phone_number varchar(20));
"""

connection = create_db_connection('localhost', 'root', pw, db)
execute_query(connection, create_orders_table)
