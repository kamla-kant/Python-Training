"""
 This is project 1 developed to
 add and sub 2 numbers
 """


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == "__main__":
    r1 = add(10, 20)
    print("r1 : ", r1)
    r2 = sub(10, 20)
    print("r2 : ", r2)

# Why _name_ ?
# - If our client run this program, they will run project_1.py
#   they will get output
# In Some Scenario where,
#   - testing team is importing this file to test add & sub,
#       during that import, we dont want to execute whatever is present
#       inside the _name_ block
#
#  - OR, assume, we may need to reuse add & sub in another project
#   that time also whatever is present inside _name_ should not execute
#
# FINALLY
# whatever present inside _name_ block
# will execute when we run this program
# will not execute when we import this program in some other file
# OR
# How it works?
# value of _name_ is _main_ when we run this program
# value of _name_ is 'filename' when we import this program