"""
 Write a program to extract
 IP
 DATE
 PICS
 URL
 from
 server_log.txt
 and
 send it to SQL database
 """

# POINT-1
'''
Databases :
 - allow us to store data
 - This can be accessed through network
'''

# POINT-2
'''
2 Types of Database
1. SQL databases : We will communicate using SQL query
    - oracle, mysql, sqlite etc
2. No-SQL databases : No SQL query. It is Dictionary or json type data
    - mongodb etc 
'''

# POINT-3
'''
python program    <---communicate-->    SQL Database Server
python program    <---communicate using library-->    SQL Database Server
python program    <---communicate using library (sqlite3)-->    SQLite Database Server
python program    <---communicate using library (pymysql)-->    MySQL Database
python program    <---communicate using library (cx_Oracle)-->    Oracle Database
'''

# POINT-4
'''
Here we will use,
python program    <---communicate using library (sqlite3)-->    SQLite Database Server
so,
we need
1) library (sqlite3) : Already present
2) Sqlite Database server : Already Present

If we any other database like mysql then
we need to install
1) mysql database
2) pymysql library
'''

# Steps
# ----------------------------------
# Step - 1 : Create database & table
# Step - 2 : Extract data
# Step - 3 : Insert into table
# Step - 4 : Save the data
# ----------------------------------

# Step - 1 : Create database & table
import sqlite3

print("Connect/Creating database 'my_db.sqlite3' ")
my_db_connection = sqlite3.connect('my_db.sqlite3')
# This will establish the connection with DB
print("Done")

# In case of sqlite3, not required to pass
# user credentials but for other databases we need to pass
# example : MySQL
# import pymysql
# con = pymysql.connect(user='',password='',host='',port='', db='')

print("Get the cursor.(It help us to send query & retreive result)")
my_db_cursor = my_db_connection.cursor()
print("Done")

print("Create a table if not exists")
my_query = '''
 CREATE TABLE IF NOT EXISTS MYLOGDATA(
 IP VARCHAR(100),
 DATE VARCHAR(100),
 PICS VARCHAR(100),
 URL VARCHAR(100)
 )
 '''
print("Done")
print("Executing Query : ", my_query)
my_db_cursor.execute(my_query)
print("Done")

print("Read Data From Server Log")
# Steps to connect to files
# 1 : Connect -open
my_log_file_handle = open("../log/server_log.txt", "r")

# 2 : Read/Write read/readlines/for loop etc
list_of_lines = my_log_file_handle.readlines()

# 3 : disconnect
my_log_file_handle.close()
print("Done")

print("# Step - 2 : Extract data")

# Below code is copied from example-7
for my_each_line in list_of_lines:
    first_three_chars = my_each_line[0:3]
    if first_three_chars.isdigit():
        sp = my_each_line.split()
        ip = sp[0]

        dt = sp[3]
        index_of_colon = dt.index(':')
        dt = dt[1:index_of_colon]

        im = sp[6]
        index_right_slash = im.rindex('/')
        im = im[index_right_slash + 1:]

        url = sp[10]
        url = url[1:-1]

        print(ip, dt, im, url)

        # Step - 3 : Insert into table
        my_query = f"INSERT INTO MYLOGDATA VALUES('{ip}', '{dt}', '{im}','{url}')"
        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        print("Done")

my_db_connection.commit()
print("All Data has been sent to DB")
print("Closing DB")
my_db_connection.close()
print("Done")