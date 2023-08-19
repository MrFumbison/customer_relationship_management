# install mysql on my pc
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Fumbison175@'
)

# prepare a cursor object
cursorobject = database.cursor()

# create a database
cursorobject.execute("CREATE DATABASE customer_database")

print("all done!")