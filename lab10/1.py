#relational databases

#data in stored in tables(also called relations)
#tables consist of rows and colums
#columss represent attributes
#rows represent entities

#in general,each table represents 1 entity type(e.g student)
#column represent arrtibutes of entity
#rows are instances of that entity

# in such databases,we can:
#create data
#read data
#update data
#delete date
#or usually refered to as crud

#RDBMS - relational database Management System
#We will PostgeSQL(also known as Postgres)as our RDBMS

#SQL - structured query language
#It is the labguage used to work with RDBMS
import psycopg2
#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = '1223'
    )
#create a cursor to work with the database
cur = conn.cursor()
#querying the database
cur.execute('SELECT Version()')
db_ver = cur.fetchall()
print(db_ver)