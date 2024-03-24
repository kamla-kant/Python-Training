"""
 Read data from mongodb
 and
 print
 and
 write to files (.txt, .csv)
 """

from pymongo import MongoClient

print("Connecting mongo db server")
my_db_connection = MongoClient(host='127.0.0.1', port=27017)
print("Done")

print("Creating/Connecting to existing database 'mytestdb2'")
db = my_db_connection['MyLogDB']
print("Done")

print("Creating/Connecting to collection 'MyCollection'")
my_collection = db["MyLogCollection"]
print("Done")

print("Getting data from db")
my_db_result = my_collection.find()
print("Done")

# Write to files
# Steps

# Step-1 : Connect
my_txt_file = open("my_mongodb_dump.txt", 'w')
my_csv_file = open("my_mongodb_dump.csv", 'w')

# Step-2 : write
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file)
print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file)

print("Writing MongoDB data to files")
for each_record in my_db_result:
    print("Writing : ", each_record)
    print(each_record["IP"], each_record["DATE"], each_record["PICS"], each_record["URL"], sep="\t", file=my_txt_file)
    print(each_record["IP"], each_record["DATE"], each_record["PICS"], each_record["URL"], sep=",", file=my_csv_file)
    print("Done")
print("All records are wrttien to files")
print("Please check my_mongodb_dump.txt and my_mongodb_dump.csv")

# Step-3 : Disconnect
my_txt_file.close()
my_csv_file.close()

print("Closing DB connection")
my_db_connection.close()
print("Done")