"""
Write Assignment2 with exceptions handling added.
Assignemnt 2 may give following error
1) if index is not present then there is a chances of IndexError, so handle it
2) if log file not present then there is a chances of FileNotFoundError, so handle it
"""

print("Trying to open Data From Server Log")
try:
    my_log_file_handle = open("../log/server_log.txt", "r")

    list_of_lines = my_log_file_handle.readlines()


    my_log_file_handle.close()
    print("Done")


    print("# Step - 2 : Extracting data")

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

            print("-" * 40)
    print("Done")

except FileNotFoundError:
    print("Given File path does not exist")
except IndexError:
    print("Some line has matched first_three_chars as digit but no other fields ")
