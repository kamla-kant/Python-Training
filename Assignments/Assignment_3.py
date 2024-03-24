"""
 Write a function which takes file path
 as an argument and
 Extract
 IP
 DATE
 PICS
 IMAGE
 and return list of tuples
 where each tuple will be one row data

 # Test
 Call the above function with '../log/server_log.txt' as argument
 and
 print then output

 # Output should look like this
 [('123.123.123.123', '20/11/2021', 'abc.jpg', 'www.google.com')
 ('123.123.123.123', '20/11/2021', 'abc.jpg', 'www.google.com'),
 ('123.123.123.123', '20/11/2021', 'abc.jpg', 'www.google.com')]
 """

def extract_data_from_file(location):
    print("Looking for Data From Given location")

    import os
    if os.path.isfile(location):
        my_log_file_handle = open(location, "r")

        list_of_lines = my_log_file_handle.readlines()

        my_log_file_handle.close()
        print("Done")

        dataList=[]
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
                dataTuple=(ip,dt,im,url)
                dataList.append(dataTuple)
        print("-" * 40)
        print(dataList)
    else:
        print("Enter a proper Location")
    print("-" * 40)
    print("Done")


extract_data_from_file("../log/server_log.txt")
