"""
 Get data from SQL DB and write to files
 """

import sqlite3

print("Connect/Creating database 'my_db.sqlite3' ")
my_db_connection = sqlite3.connect('my_db.sqlite3')
print("Done")

print("Get the cursor.(It help us to send query & retreive result)")
my_db_cursor = my_db_connection.cursor()
print("Done")

my_query = "SELECT * FROM MYLOGDATA"
print("Executing Query : ", my_query)
my_db_cursor.execute(my_query)
print("Done")

print("Reading all data from cursor")
my_db_result = my_db_cursor.fetchall()
print("Done")

print("my_db_result : ", my_db_result)

print("-" * 40)
# ---------------------------

# There are many ways to write to files
# 1-way
print("1-way: Write to files")
print("-" * 40)
# ---------------------

# Steps
# 1) Connect
my_file_handle = open("db_dump_1.txt", 'w')

# 2) for Write we can use 1) write 2) writelines 3) print
# Write header
my_file_handle.writelines(["IP\t", "DATE\t", "PICS\t", "URL\n"])
# print("IP", "DATE", "PICS", "URL", sep="\t", file=my_file_handle)
for each_row in my_db_result:
    print(each_row[0], each_row[1], each_row[2], each_row[3], file=my_file_handle)

# 3) Disconnect
my_file_handle.close()

print('db_dump_1.txt created Successfully. Please Check')

print("-" * 40)
# ---------------------

print("2nd-Way using Pandas Library")
print("-" * 40)
# ---------------------
# About Pandas
##############
# - Inside pandas we have 1 class called 'DataFrame'
# - Inside DataFrame class, we have methods releated to 2Dimentional data
#   like excel/table data where rows & columns
# - Inside 'DataFrame' class we have methods like to_csv, to_excel,
#   to_json to create files
# - Means, calling one method will create files, No need for loop and all

# Install Libraires from pypi
##############
# 1) pandas
# 2) openpyxl

# How to install
##############
# 1-way : execute command in cmd prompt
#   - pip install pandas
#   - pip install openpyxl
#
# 2- way : through pycharm
#   -Goto File-> Settings -> Project:python training ->
#       -> python interpreter -> Click on '+' -> type library name
#       -> click on install
##############

import pandas as pd

print("my_df : ")
print("-" * 20)
# -----------------

my_df = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
print(my_df)

print("-" * 20)
# -----------------

print("Methods inside DataFrame Class")
print(dir(my_df))

print("-" * 20)
# -----------------

print("my_df_2 : ")
print("-" * 20)
# -----------------

my_df_2 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=['myrow1', 'myrow2'], columns=['mycol1', 'mycol2', 'mycol3'])
print(my_df_2)

print("-" * 20)
# -----------------
print("my_log_data_df : ")
print("-" * 20)
# -----------------
# Create Dataframe with my_db_result data
my_log_data_df = pd.DataFrame(my_db_result, columns=["IP", "DATE", "PICS", "URL"])
print(my_log_data_df)

print("-" * 20)
# -----------------

print("Dumping data to files")
print("-" * 20)
# -----------------

my_log_data_df.to_csv("db_dump_2.txt", sep="\t")
my_log_data_df.to_csv("db_dump_3.csv")  # Default sep=","
my_log_data_df.to_excel("db_dump_4.xlsx")
my_log_data_df.to_json("db_dump_5.json")

print("Log Files db_dump_2.txt, db_dump_3.csv, db_dump_4.xlsx, db_dump_5.json created")
print("Please Check")

print("-" * 40)
# ---------------------