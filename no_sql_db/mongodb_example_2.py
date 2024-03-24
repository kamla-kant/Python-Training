"""
Read data directly from website
and
extract
IP
DATE
PICS
URL
and insert into mogodb
"""
# Steps
'''
Step - 1. Read from URL
Step - 2. Extract IP, DATE, PICS, URL
Step - 3. Send extracted Data to mongDB 
'''
# Step - 1. Read from URL
import urllib.request as u
my_url = 'http://www.jafsoft.com/searchengines/log_sample.html'
my_website_file_handle = u.urlopen(my_url)
# We can call read, readlines etc to read
# Here we are reading using for loop
# for loop will take care of reading line by line
# SOME PROBLEM
'''
We tought of copying code from example_7,
BUT 
if first_three_chars.isdigit():, This condition is failing
because data is coming as html page source where
some other lines also starting with 3 digits
So this wont work
'''
# SOLUTION to ABOVE PROBLEM
'''
1. Use regular expression 
2. Use library BeautifulSoup
    (From BeautifulSoup library we can travese through each tag)
    Steps:
    1. get <PRE> tag data
    2. then extract using ex_7 code or write regular expression 
'''
#################################
# Start : BeautifulSoup Library Tasks
#################################
print("Start : BeautifulSoup Library Tasks")

my_url = 'http://www.jafsoft.com/searchengines/log_sample.html'
my_website_file_handle = u.urlopen(my_url)
from bs4 import BeautifulSoup

print("Obtaining BeautifulSoup object")
soup = BeautifulSoup(my_website_file_handle, 'html.parser')
print("Done")

print("Soup :")
print("-" * 20)
# ----------------------

print(soup)

print("-" * 40)
# ----------------------

print("Head Tag :")
print("-" * 20)
# ----------------------

print(soup.head)

print("-" * 40)
# ----------------------

print("Title in Head Tag :")
print("-" * 20)
# ----------------------

print(soup.head.title)

print("-" * 40)
# ----------------------

print("Title text in Head Tag :")
print("-" * 20)
# ----------------------

print(soup.head.title.text)

print("-" * 40)
# ----------------------

print("link in Head Tag :")
print("-" * 20)
# ----------------------

print(soup.head.link)  # We have more link tags, first one will come

print("-" * 40)
# ----------------------

print("link tag attributes Head Tag :")
print("-" * 20)
# ----------------------

print("REL : ", soup.head.link['rel'])
print("HREF : ", soup.head.link['href'])

print("-" * 40)
# ----------------------
print("All link tags in Head Tag :")
print("-" * 20)
# ----------------------

all_links = soup.head.find_all('link')

for each_link in all_links:
 print("each_link : ", each_link)
 print("each_link REL : ", each_link['rel'])
 print("each_link HREF : ", each_link['href'])
 print("-" * 10)

print("-" * 40)
# ----------------------

print("Our Required Log Data (inside PRE tag)")
print("-" * 40)
# ----------------------

our_log_data = soup.body.pre.text
print("our_log_data")
print(our_log_data)

print("type of data : ", type(our_log_data))

print("-" * 40)
# ----------------------
print("End : BeautifulSoup Library Tasks")
#################################
# End : BeautifulSoup Library Tasks
#################################
print("-" * 40)
# ----------------------
# Create mongodb database and collection
# Below code Copied from mongodb_example_2
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

# our_log_data is coming as string, so we
# can use example_7 code
print("Get list of lines")
print("-" * 40)
# ----------------

list_of_lines = our_log_data.split("\n")
print(list_of_lines)

print("-" * 40)
# ----------------
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
  my_data = {"IP": ip, "DATE": dt, "PICS": im, "URL": url}
  print(f"Inserting data {my_data}")
  my_collection.insert_one(my_data)
  print("Done")

print("All records added mongoDB")
print("Closing DB connection")
my_db_connection.close()
print("Done")

# Convert from bytes to string
'''
data = b'hello'
>>> type(data)
<class 'bytes'>
>>> # Methods inside bytes class
>>> dir(data)
['_add', 'class', 'contains', 'delattr', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'getitem', 'getnewargs', 'gt', 'hash', 'init', 'init_subclass', 'iter', 'le', 'len', 'lt', 'mod', 'mul', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'rmod', 'rmul', 'setattr', 'sizeof', 'str', 'subclasshook_', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # Convert to string
>>> data = data.decode()
>>> 
>>> type(data)
<class 'str'>
>>> 
'''