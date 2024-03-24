"""
 Solve Assignemnt_5.py using
 mongodb database
 """

from pymongo import MongoClient

print("Connecting mongo db server")
mongodb_connection = MongoClient(host='127.0.0.1', port=27017)
print("Done")

db = mongodb_connection['student_db']
print("Done")

print("Creating/Connecting to collection 'student_table'")
student_collection = db["student_table"]
print("Done")
student_collection.drop()
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

        my_data = {"NAME": nm, "SEAT NO":sn, "S1":s1, "S2":s2}

        # Step - 3 : Insert into table
        print(f"Inserting data {my_data}")
        student_collection.insert_one(my_data)
        print("Done")


print("Getting data from db")
my_db_result = student_collection.find()
print("Done")

print("Display the data")
dataList=[]
for each_record in my_db_result:
    print(each_record)
    dataList.append([each_record["NAME"],(int(each_record["S1"])+int(each_record["S1"].strip("/n")))/2])
print("Done")

import pandas as pd
student_data_df = pd.DataFrame(dataList, columns=["NAME", "AVERAGE"])
print(student_data_df)

print("Closing DB connection")
mongodb_connection.close()
print("Done")