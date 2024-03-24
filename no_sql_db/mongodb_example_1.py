"""
 mongodb_example_1.py
 """

from pymongo import MongoClient

print("Connecting mongo db server")
my_db_connection = MongoClient(host='127.0.0.1', port=27017)
print("Done")

print("Creating/Connecting to existing database 'mytestdb2'")
db = my_db_connection['mytestdb2']
print("Done")

print("Creating/Connecting to collection 'MyCollection'")
my_collection = db["MyCollection"]
print("Done")

my_data = {"A": 10}
print(f"Inserting data {my_data}")
my_collection.insert_one(my_data)
print("Done")

print("Getting data from db")
my_db_result = my_collection.find()
print("Done")

print("Display the data")
for each_record in my_db_result:
    print(each_record)
print("Done")

print("Closing DB connection")
my_db_connection.close()
print("Done")