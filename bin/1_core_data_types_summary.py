"""
Summary of Core Data Types
"""

# Core Data Types : Already some options are available to
# store data
# 1. Numbers
# 2. Strings
# 3. list
# 4. tuple
# 5. dict
# 6. set
# 7. frozenset

print("1. Numbers")
print("-"*40)
# --------------------
# Already option to store numbers
# how?
a = 10 # internally calls class name to create
# or
b = int(10)

print(a, b)

print("-"*40)
# --------------------

print("# 2. Strings")
print("-" * 40)
# --------------------
# Already option to store collection of characters
# how?
s1 = 'python'
s2 = str('python')
print(s1, s2)

# 3. Classes (Group of 1. Variables and # 2. Functions)
# what is there inside str class?
print("Inside str class(Group of 1. Variables and # 2. Functions)")
print(dir(s1))

'''
>>> dir(s1)
['_add', 'class', 'contains', 'delattr', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'getitem', 'getnewargs', 'gt', 'hash', 'init', 'init_subclass', 'iter', 'le', 'len', 'lt', 'mod', 'mul', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'rmod', 'rmul', 'setattr', 'sizeof', 'str', 'subclasshook_', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
'''

# Why naming convention __
# names which is starting with _ & ending with _ are
# internally some function/operators are calling
# Just say that theses methods are being called internally,
# they are using naming convetion __

# Example:
# >>> s1="Hello"
# >>>
# >>> s2 = "Python"
# >>> s1+s2
# 'HelloPython'
# >>> # + is internally calling _add_
# >>> # Manually also we can call
# >>> s1._add_(s2)
# 'HelloPython'
# >>>

print("Using one method")
s3 = 'hello'
print("s3 is : ", s3)
s4 = s3.upper()
print("s4 is : ", s4)

print("-" * 40)
# --------------------

print("3. List")
print("-" * 40)
# --------------------
# help us to store more than one lement
# It is MUTABLE
L1 = [10, 20, 30, 40]
L2 = list([10, 20, 30, 40])

print("L1 & L2 are : ", L1, L2)

# Any Program can have either
# 1. Variables
# 2. Functions
# 3. Classes (Group of 1. Variables and # 2. Functions)

print("Methods inside list class")
print(dir(L1))

print("-" * 40)
# ------------------------------

print("4. Tuple")
print("-" * 40)
# ------------------------------
# help us to store more than one lement
# It is IMMUTABLE

T1 = (10, 20, 30, 40)
T2 = tuple([10, 20, 30, 40])

print("T1 & T2 are : ", T1, T2)

# Any Program can have either
# 1. Variables
# 2. Functions
# 3. Classes (Group of 1. Variables and # 2. Functions)

print("Methods inside tuple class")
print(dir(T1))

print("-" * 40)
# ------------------------------

print("5. dict")
print("-" * 40)
# ------------------------------
# Key/Value
D1 = {"A": 10, "B": 20}
D2 = dict({"A": 10, "B": 20})

print(D1, D2)

# Any Program can have either
# 1. Variables
# 2. Functions
# 3. Classes (Group of 1. Variables and # 2. Functions)

print("Methods inside dict class")
print(dir(D1))
print("-" * 40)
# ------------------------------

print("5.Set")
print("-" * 40)
# ------------------------------
# IMMUTABLE

S1 = {10, 20, 20, 20, 20}  # if we give key:value then dict
S2 = set({10, 20, 20, 20, 20})
print(S1, S2)

# Any Program can have either
# 1. Variables
# 2. Functions
# 3. Classes (Group of 1. Variables and # 2. Functions)
print(dir(S1))
print("-" * 40)
# ------------------------------

print("6.FrozeSet")
print("-" * 40)
# ------------------------------
# IMMUTABLE
S1 = frozenset({10, 20, 20, 20, 20})
print(S1)

# Any Program can have either
# 1. Variables
# 2. Functions
# 3. Classes (Group of 1. Variables and # 2. Functions)
print(dir(S1))
print("-" * 40)
# ------------------------------