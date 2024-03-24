"""
 In this project, we are making use
 of functions & variables present in MyModule.py
 """

print("1-way to import")
print("-" * 40)
# ----------------------
import MyModule

print("Company Name : ", MyModule.my_company)
print("add of 10 20 : ", MyModule.add(10, 20))
print("-" * 40)
# ----------------------

print("2-way to import")
print("-" * 40)
# ----------------------
import MyModule as mm

print("Company Name : ", mm.my_company)
print("add of 10 20 : ", mm.add(10, 20))
print("-" * 40)
# ----------------------

print("3-way to import")
print("-" * 40)
# ----------------------
from MyModule import my_company, add

print("Company Name : ", my_company)
print("add of 10 20 : ", add(10, 20))
print("-" * 40)
# ----------------------


print("4-way to import")
print("-" * 40)
# ----------------------
from MyModule import my_company as mc, add as ad

print("Company Name : ", mc)
print("add of 10 20 : ", ad(10, 20))
print("-" * 40)
# ----------------------


print("5-way to import")
print("-" * 40)
# ----------------------
from MyModule import *

print("Company Name : ", my_company)
print("add of 10 20 : ", add(10, 20))
print("-" * 40)
# ----------------------

# PACKAGE IMPORT

print("1-way to import")
print("-" * 40)
# ----------------------
import MyPackage.aws.MyModule

print("Company Name : ", MyPackage.aws.MyModule.my_company)
print("add of 10 20 : ", MyPackage.aws.MyModule.add(10, 20))
print("-" * 40)
# ----------------------

print("2-way to import")
print("-" * 40)
# ----------------------
import MyPackage.aws.MyModule as mm

print("Company Name : ", mm.my_company)
print("add of 10 20 : ", mm.add(10, 20))
print("-" * 40)
# ----------------------

print("3-way to import")
print("-" * 40)
# ----------------------
from MyPackage.aws.MyModule import my_company, add

print("Company Name : ", my_company)
print("add of 10 20 : ", add(10, 20))
print("-" * 40)
# ----------------------

print("4-way to import")
print("-" * 40)
# ----------------------
from MyPackage.aws.MyModule import my_company as mc, add as ad

print("Company Name : ", mc)
print("add of 10 20 : ", ad(10, 20))
print("-" * 40)
# ----------------------

print("5-way to import")
print("-" * 40)
# ----------------------
from MyPackage.aws.MyModule import *

print("Company Name : ", my_company)
print("add of 10 20 : ", add(10, 20))
print("-" * 40)
# ----------------------