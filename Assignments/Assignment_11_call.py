"""
Create a module using functions defined in assignemnt_4
and class defined in Assignemnt_7.
create another python file, import and call the
class & functions. display the result
"""

import Assignment_11 as a11
print(a11.extract_IPs("../log/server_log.txt"))
print(a11.extract_Dates("../log/server_log.txt"))

print("-"*100)

a11_methods=a11.Assignment7("../log/server_log.txt")
print(a11_methods.get_ips())
print(a11_methods.get_dates())
print(a11_methods.get_pics())
print(a11_methods.get_urls())