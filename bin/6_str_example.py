"""
 From
 below string

 extract
 IP
 DATE
 PICS
 URL

 and
 print
 """

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

print("What kind of data we have")

print("-" * 40)
# --------------------

print(type(in_string))

print("-" * 40)
# --------------------

print("Check whether methods inside str class will be helpful")
print("to this requirement?")
print("List of methods : ")
print("-" * 40)
# --------------------

print(dir(in_string))

print("-" * 40)
# --------------------

print("Extracting Info")
print("-" * 40)
# --------------------
sp = in_string.split()
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

print("-" * 40)
# --------------------


###########################
# COMMENTS
###########################
'''
in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

dir(in_string)
['_add', 'class', 'contains', 'delattr', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'getitem', 'getnewargs', 'gt', 'hash', 'init', 'init_subclass', 'iter', 'le', 'len', 'lt', 'mod', 'mul', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'rmod', 'rmul', 'setattr', 'sizeof', 'str', 'subclasshook_', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# There are Many ways to do
# 1 - way to extract IP
ip[0:14]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ip[0:14]
NameError: name 'ip' is not defined. Did you mean: 'id'?
in_string[0:14]
'123.123.123.12'
in_string[0:15]
'123.123.123.123'

# 2- way to extract IP
sp = in_string.split()
sp
['123.123.123.123', '-', '-', '[26/Apr/2000:00:23:48', '-0400]', '"GET', '/pics/wpaper.gif', 'HTTP/1.0"', '200', '6248', '"http://www.jafsoft.com/asctortf/"', '"Mozilla/4.05', '(Macintosh;', 'I;', 'PPC)"']
in_string[0]
'1'
sp[0]
'123.123.123.123'

# Extract Date
dt = sp[3]
dt
'[26/Apr/2000:00:23:48'
index_of_colon = dt.index(':')
index_of_colon
12
dt = dt[1:index_of_colon]
dt
'26/Apr/2000'

# Extract Image
# 1 - Way
im = sp[6]
im
'/pics/wpaper.gif'
# remove /pics/ - 1st - way
# find index of 'from right first slash'
index_right_slach = im.rindex('/')

 = im.rindex('/')
SyntaxError: unexpected indent
index_right_slash = im.rindex('/')
index_right_slash
5
im1 = im[index_right_slash + 1 : ] # index 6 to end
im1
'wpaper.gif'

# remove /pics/ - 2nd - way
im2 = im.lstrip('/pics/')
im2
'wpaper.gif'

# remove /pics/ - 3rd - way
im3 = im.split('/')
im3
['', 'pics', 'wpaper.gif']
im3[2]
'wpaper.gif'
im3[-1]
'wpaper.gif'

# remove /pics/ - 4th - way
im4 = im.replace('/pics/', '')
im4
'wpaper.gif'

# URL
url = sp[10]
url
'"http://www.jafsoft.com/asctortf/"'
# Remove " from string
# We can make use of above ways
url = url[1:-1]
url
'http://www.jafsoft.com/asctortf/'
print(url)
http://www.jafsoft.com/asctortf/

'''