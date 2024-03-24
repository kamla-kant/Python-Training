"""
 Write a program
 #1
 which creates student_db in sqlite3 database
 and also create table 'student_table' with below columns
 Name
 seat no
 sub1_marks
 sub2_marks
 #2
 read data from student_marks.csv
 and push to above table
 IF STUDENT SEAT_NO IS ALREADY PRESENT THEN DONT INSERT
 #3
 read data from above table
 and display

 student name        average marks
 s1                   75
 etc
 """

import sqlite3

print("Connect/Creating database 'student_db' ")
db_connection = sqlite3.connect('student_db.sqlite3')
# This will establish the connection with DB
print("Done")

print("Get the cursor.(It help us to send query & retreive result)")
db_cursor = db_connection.cursor()
print("Done")

print("Create a table if not exists")
query = '''
 CREATE TABLE IF NOT EXISTS student_table(
 NAME VARCHAR(100),
 SEAT_No VARCHAR(100),
 Sub_Marks1 VARCHAR(100),
 Sub_Marks2 VARCHAR(100)
 )
 '''
print("Done")
print("Executing Query : ", query)
db_cursor.execute(query)
print("Done")

csv_file_handle = open("student_marks.csv", "r")

# 2 : Read/Write read/readlines/for loop etc
list_of_rows = csv_file_handle.readlines()

# 3 : disconnect
csv_file_handle.close()
print("Done")

for each_student in list_of_rows:
        s = each_student.split(",")
        print(s)
        nm = s[0]

        sn = s[1]

        s1 = s[2]

        s2 = s[3]

        print(nm, sn, s1, s2)

        # Step - 3 : Insert into table
        insert_query = f"INSERT INTO student_table VALUES('{nm}', '{sn}', '{s1}','{s2}')"
        print("Executing Query : ", insert_query)
        db_cursor.execute(insert_query)
        print("Done")

db_connection.commit()
print("All Data has been sent to DB")

extract_query = "SELECT * FROM student_table"
print("Executing Query : ", extract_query)
db_cursor.execute(extract_query)
print("Done")

print("Reading all data from cursor")
db_result = db_cursor.fetchall()
print("Done")
print("Closing DB")
db_connection.close()

#Fetching Result
display_result=[]
for each in db_result:
    display_result.append([each[0], ((int(each[2])+int(each[3].strip('\n')))/2)])
print(display_result)

#Displaying result
import pandas as pd
student_data_df = pd.DataFrame(display_result, columns=["NAME", "AVERAGE"])
print(student_data_df)
