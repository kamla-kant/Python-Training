"""
 Create a module with
 4 functions inside the module

 Function-1 :
 # -------------------
 Write a function which takes file path
 as an argument and
 Extract
 IP
 return list of IPS

 Function-2 :
 # -------------------
 Write a function which takes file path
 as an argument and
 Extract
 IP
 return list of Dates

 Import in another program and pass server_log.txt path
 to each function and print the result of both the functions
 """

def extract_IPs(location):
    import os
    if os.path.isfile(location):
        my_log_file_handle = open(location, "r")

        # 2 : Read/Write read/readlines/for loop etc
        list_of_lines = my_log_file_handle.readlines()

        # 3 : disconnect
        my_log_file_handle.close()

        # Below code is copied from example-7
        ipList = []
        for my_each_line in list_of_lines:
            first_three_chars = my_each_line[0:3]
            if first_three_chars.isdigit():
                sp = my_each_line.split()
                ip = sp[0]
                ipList.append(ip)
        return ipList
    else:
        print("Enter a proper Location")
    print("-" * 40)
    print("Done")

def extract_Dates(location):
    import os
    if os.path.isfile(location):
        my_log_file_handle = open(location, "r")

        list_of_lines = my_log_file_handle.readlines()

        my_log_file_handle.close()

        dateList = []
        for my_each_line in list_of_lines:
            sp=my_each_line.split()
            for data in sp:
                if ((len(data)>7)and(data[3]=="/" and data[7]=="/")):
                    index_of_colon = data.index(':')
                    dt = data[1:index_of_colon]
                    dateList.append(dt)
        return (dateList)
    else:
        print("Enter a proper Location")
    print("-" * 40)
    print("Done")


if __name__ == "__main__":
    print(extract_IPs("../log/server_log.txt"))
    print(extract_Dates("../log/server_log.txt"))