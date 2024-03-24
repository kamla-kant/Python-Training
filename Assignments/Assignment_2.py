'''write a program to read data
from server.log.txt and extract
ip
date
pics
url
and write to output file "serverlogreport.txt"
'''

print("Read Data From Server Log")

my_log_file_handle = open("../log/server_log.txt", "r")

list_of_lines = my_log_file_handle.readlines()


my_log_file_handle.close()
print("Done")

print("# Step - 2 : Extract data")

print("Writing to serverlogreport.txt")
my_log_file_handle = open("../log/serverlogreport.txt", "w")

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

        print(" IP: ", ip, "\n DATE: ", dt, "\n IMAGE: ", im, "\n URL: ", url)
        my_log_file_handle.writelines(" IP: "+ repr(ip)+ "\n DATE: "+ repr(dt)+ "\n IMAGE: "+ repr(im)+ "\n URL: "+ repr(url))

        print("-" * 40)
print("Done")