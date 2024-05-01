#create -insert
#read - select
#delete - delete
#update - update
import psycopg2
#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "1223",
    port =5433
    )
#create a cursor to work with the database
cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute('DROP TABLE students_data;')
conn.commit()


#create a new table
cur.execute("""create table if not exists students_data(
            name varchar(255),
            phone_number varchar(20)
        
);
""")
conn.commit()
#create new students
cur.execute("""insert into students_data (name, phone_number) VALUES
            ('ruslan','+77766666'),
            ('maris','+777664326')
""")
conn.commit()
cur.execute('select name,phone_number from students_data')
print(cur.fetchall())
# #update students
# cur.execute("""update students_data
#             set name = 'almas'
#             where name= 'ruslan'
# """)
# conn.commit()
# #delete students table
# cur.execute("""delete from students_data
#             where name = 'maris'
# """)