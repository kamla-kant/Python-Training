"""
Final Summary 1
"""

print("Core Data Types")
print("1. Numbers")
print("-"*20)
# -------------------------

a = 10
b = int(10)
print(a, b)

print("-"*40)
# -------------------------

print("2. Strings")
print("-"*20)
# -------------------------

a = 'python'
b = str('python')
print(a,b)

# - 2 Indexes to each char +ve & -ve index
# - Using index we can access single characters
# - get sub string
# - step
# - traverse left to right & right to left

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

print("Methods inside the class")
print(dir(a))

print("-"*40)
# -------------------------

print("3. List")
print("-"*20)
# -------------------------

a = [10, 20, 30]
b = list([10, 20, 30])
print(a,b)

# - 2 Indexes to each  +ve & -ve index
# - Using index we can access single element
# - get sub list
# - step
# - traverse left to right & right to left

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

print("Methods inside the class")
print(dir(a))

print("-"*40)
# -------------------------


print("4. Tuple")
print("-"*20)
# -------------------------

a = (10, 20, 30)
b = tuple([10, 20, 30])
print(a,b)

# - 2 Indexes to each  +ve & -ve index
# - Using index we can access single element
# - get sub list
# - step
# - traverse left to right & right to left

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

print("Methods inside the class")
print(dir(a))

print("-"*40)
# -------------------------

print("5. Dictionary")
print("-"*20)
# -------------------------

a = {"a": 10, "b": 20, "c": 30}
b = dict({"a": 10, "b": 20, "c": 30})
print(a, b)

# No Index

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

print("Methods inside the class")
print(dir(a))

print("-"*40)
# -------------------------

print("6. set")
print("-"*20)
# -------------------------

a = {10, 20, 30}
b = set({10, 20, 30})
print(a, b)

# No Index

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

print("Methods inside the class")
print(dir(a))

print("-"*40)
# -------------------------

print("7. frozenset")
print("-"*20)
# -------------------------

a = frozenset({10, 20, 30})
b = frozenset({10, 20, 30})
print(a, b)

# No Index

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

print("Methods inside the class")
print(dir(a))

print("-"*40)
# -------------------------

print("Conditional statement - if")
print("-"*20)
# -------------------------
a = 10
b = "Python"
c = [100, 200, 300]
d = {"A": 10, "B": 20}

# 1 - way
if a == 10:
    print("a is 10")
elif a > 10:
    print("a gt 10")
else:
    print("a lt 10")

# 2 - way
if (    (a == 10) and
        (b == "Python") and
        ("tho" in b) and
        (len(c) > 0) and
        (200 in c) and
        ("A" in d) and
        ("A" in d.keys()) and
        (20 in d.values()) and
        (("A", 10) in d.items())
    ):
    print("all are true")

print("-"*40)
# -------------------------

print("for-loop")
print("-"*20)
# -------------------------

# Iterate any collection
L = [10, 20, 30, 40]

# 1
for i in L:
    print("i : ", i)

# 2 break : to stop in between
for j in L:
    print("j : ", j)
    if j > 20:
        break

# 3 continue : skip current iteration and go for next iteration
for k in L:
    if k%2 != 0:
        continue
    print("k : ", k) # only even numbers will get printed

print("-"*40)
# -------------------------
print("while-loop")
print("-"*20)
# -------------------------

# Based on condition, execute the loop
L = [10, 20, 30, 40]

# 1
i = 0
while i < len(L):
    print("i value : ", L[i])
    i = i + 1

# 2 break : to stop in between
j = 0
while j < len(L):
    print("j value : ", L[j])
    if L[j] > 20:
        break
    j = j + 1

# 3 continue : skip current iteration and go for next iteration
k = 0
while k < len(L):
    if L[k]%2 != 0:
        k = k + 1
        continue
    print("k value : ", L[k])
    k = k + 1

print("-"*40)
# -------------------------
# -------------------------
# Till here, we were storing data in variables
# once program execution is completed, all the data is getting cleaned up.
#
# Now,
# We are trying to communicate with external sources like files, database, other systems etc
# If we are communicating with any external sources then we need to follow below 3 steps
# Steps :
# Step - 1 : Connect
# Step - 2 : Communicate
# Step - 3 : Disconnect
# -------------------------

# -------------------------
# Example : text files with any extension like .txt, .csv, .log etc
#
# Steps :
# Step - 1 : Connect
#       - open function
# Step - 2 : Communicate(Read/Write)
#       - Write : 1) write function 2) writelines function  3) print function
#       - Read : 1) read 2) readline 3) readlines 4) pass file handle in for
# Step - 3 : Disconnect
#       - Only Save : flush()
#       - Save & Disconnect : close()
# -------------------------

# -------------------------
# Example : SQL & No-SQL
# Steps :
# Step - 1 : Connect
#       - connect function
# Step - 2 : Communicate(Read/Write)
#       - SQL - Queries to send & receive
#       - No-SQL - Communicating through db object
# Step - 3 : Disconnect
#       - Only Save : commit()
#       - Save & Disconnect : close()
# -------------------------

print("Write 10 & python to my_out_file.txt")
print("-"*20)
# -------------------------
# Example : text files with any extension like .txt, .csv, .log etc
# Write 10 & python to file
# Steps :

# Step - 1 : Connect
#       - open function
my_file_handle = open("my_out_file.txt", "w")

# Step - 2 : Communicate(Read/Write)
#       - Write : 1) write function 2) writelines function  3) print function
#       - Read : 1) read 2) readline 3) readlines 4) pass file handle in for
x = 10
x = str(x) + "\n"
# why str(x) because, write expects string
s = "python\n"
my_file_handle.write(x)
my_file_handle.write(s)

# Step - 3 : Disconnect
#       - Only Save : flush()
#       - Save & Disconnect : close()
my_file_handle.close()

print("Write 10 & python to my_out_file.txt COMPLETED. Please Check the file")
print("-"*40)
# -------------------------

print("Reading my_out_file.txt")
print("-"*20)
# -------------------------
# Example : text files with any extension like .txt, .csv, .log etc
# Steps :

# Step - 1 : Connect
#       - open function
my_file_handle = open("my_out_file.txt", "r")

# Step - 2 : Communicate(Read/Write)
#       - Write : 1) write function 2) writelines function  3) print function
#       - Read : 1) read 2) readline 3) readlines 4) pass file handle in for

file_content = my_file_handle.read()
print("file_content : ", file_content)

# Step - 3 : Disconnect
#       - Only Save : flush()
#       - Save & Disconnect : close()
my_file_handle.close()

print("Reading data from my_out_file.txt COMPLETED. Please verify the output")
print("-"*40)
# -------------------------

# -------------------------
# Functions : If we want to repeat/rewrite same code more than one time
# then, instead of repeating/rewriting that code, keep that code in a block
# and use whenever we want. This block we called as function.


print(" 1 : Functions without arguments")
print("-"*20)
# ----------------------------
def add():
    a = 10
    b = 20
    c = a + b
    print("c : ", c)

add()

print("-"*40)
# ----------------------------

print(" 2 : Functions with arguments")
print("-"*20)
# ----------------------------
def add(a,b):
    c = a + b
    print("c : ", c)

add(10,20)

print("-"*40)
# ----------------------------


print(" 3 : Functions with arguments with default values")
print("-"*20)
# ----------------------------
def add(a,b=10):
    c = a + b
    print("c : ", c)

add(10)
add(10,20)

print("-"*40)
# ----------------------------

print(" 4 : Functions with arguments with default values and Variable args")
print("-"*20)
# ----------------------------
def add(a,b=10, *c):
    result = a + b + sum(c)
    print("result : ", result)

add(10)
add(10,20)
add(10,20,30,40,50,60)

print("-"*40)
# ----------------------------

print(" 5 : Functions with arguments with default values and Variable args and keyword args")
print("-"*20)
# ----------------------------
def add(a,b=10, *c, d, e=10):
    result = a + b + sum(c) + d + e
    print("result : ", result)

add(10, d=10)
add(10,20, d=10)
add(10,20,30,40,50,60, d=70, e=80) # Mentining arg name is mandatory

print("-"*40)
# ----------------------------

print(" 6 : with variable keyword args")
print("-"*20)
# ----------------------------
def add(a,b=10, *c, d, e=10, **f):
    result = a + b + sum(c) + d + e + sum(f.values())
    print("result : ", result)

add(10, d=10)
add(10,20, d=10)
add(10,20,30,40,50,60, d=70, e=80, x=100, y=200, z=300)

print("-"*40)
# ----------------------------

# ----------------------------
# Functions : same code more than one time
# Modules : same code more than one file
#   - collection of variables, functions & classes which can reused in another program
#   - 2 ways to import
#   - 1-way : import module_name
#   - 2-way : from module_name import func, class, var
# Packages : folder which is having modules & sub packages with modules
#   - 2 ways to import
#   - 1-way : import package.subpackage.module_name
#   - 2-way : from package.subpackage.module_name import func, class, var
# ----------------------------

# ----------------------------
# Classes :

# Any Program can have
# 1) Variables
# 2) Functions
# 3) Classes (Group of 1) Variables and 2) Functions)

class Student:
    college_name = "xyz engineering college"
    def __init__(self, n):
        self.name =n
    def add_marks(self, m):
        self.marks = m
    def view_marks(self):
        return self.marks

# Observations:
# Encapsulation : We are grouping student related functions & variables in one block
# Abstraction : Create object & through object we can communicate
# Example:
s1 = Student("Varshanth")
s1.add_marks(90)
print("stundent 1 marks : ", s1.view_marks())

s2 = Student("Reddy")
s2.add_marks(90)
print("stundent 2 marks : ", s2.view_marks())

# We can create n number of objects to keep each student data seperately
# Inheritance : tomorow if we want add something to class then not
# not required to rewrite instead we can extend and create new class

class NewStudent(Student):
    def add_int_marks(self, im):
        self.int_marks = im
    def view_int_marks(self):
        return self.int_marks
    def view_marks(self): # POLYMORPHISM : it allows to use same name as super class
        # this view_marks will override super class view_marks
        return self.marks + self.int_marks

s1 = NewStudent()
s1.add_marks(90)
s1.add_int_marks(25)
print("stundent 1 marks : ", s1.view_marks())
print("stundent 1 int marks : ", s1.view_int_marks())

# ----------------------------

# ----------------------------
print("-"*40)

print("Exceptions Handling :")
print("-"*20)
# ----------------------------
# Exceptions Handling :
# Problem : if any error in the program then program use to terminate
#           on that point
# Exceptions Handling : If any error program will not terminate instead
#           control will goto another block called 'except'
try:
    a = 10
    b = 0
    c = a/b # PROGRAM WILL NOT TERMINATE HERE, INSTEAD CONTROL WILL GOTO except block
    # raise ZeroDivisionError
    # assert a == 10, "message : a is zero"
except ZeroDivisionError:
    print("It is ZDE")
# Combinations
# - we can use try-except
# - we can use try-except-else
# - we can use try-except-finally
# - we can use 'raise' to throw exception manually
# - we can use 'assert' to check condition and if fails throw assertion error
print("-"*40)
# ----------------------------
