import mysql.connector

try:
    # 1. Connect using your Workbench credentials
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="omprakash1212",
        database='indigo'
    )
    mycursor = conn.cursor()
    print("Connection established")
        # 3. This proves it's actually working
except Exception as e:
    # 4. This will tell us the EXACT reason if it fails
    print(f"Connection error: {e}")
#create a database on the dbserver
#mycursor.execute('create database indigo')
#conn.commit()

# to create a table
#ariport id/cose/namee
# mycursor.execute("""
# CREATE TABLE airport(
# airport_id INTEGER PRIMARY KEY,
# code VARCHAR(10) NOT NULL,
# city VARCHAR(55) NOT NULL,
# name varchar(255) NOT NULL
# )
# """)
#conn.commit()

#insert data into the table
# mycursor.execute("""
# insert into  airport values
#     (1,'del','Hyderbad','gandhiairport'),
#     (2,'ccu','delhi','nehru'),
#     (3,'bom','mumbai','CSMA')
# """)
# conn.commit()

# search/retrive
# mycursor.execute('select * from airport where airport_id>1')
# data=mycursor.fetchall()
# # print(data)
# for i in data:
#     print(i[2])

#update
# mycursor.execute("""update airport
# set city='Bombay'
# where airport_id=3
# """)
# conn.cursor()
# mycursor.execute('select * from airport where airport_id>1')
# data=mycursor.fetchall()
# print(data)

#delete tuple or row
mycursor.execute("""delete from airport
where airport_id=3
""")
conn.commit()
mycursor.execute('select * from airport where airport_id>1')
data=mycursor.fetchall()
print(data)