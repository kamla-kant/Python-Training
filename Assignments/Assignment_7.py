"""
Write a class a which is having following 4 methods init
1) get_ips
2) get_dates
3) get_pics
4) get_urls
5) write init, which takes file_path as an argument

Outside the class, create object the class,
then print output of all 4 methods
"""

class Assignment7:

        def __init__(self,file_path):
                self.location=file_path

        def get_ips(self):
                import os
                if os.path.isfile(self.location):
                        my_log_file_handle = open(self.location, "r")

                        # 2 : Read/Write read/readlines/for loop etc
                        list_of_lines = my_log_file_handle.readlines()

                        # 3 : disconnect
                        my_log_file_handle.close()

                        # Below code is copied from example-7
                        ipsList = []
                        for my_each_line in list_of_lines:
                                first_three_chars = my_each_line[0:3]
                                if first_three_chars.isdigit():
                                        sp = my_each_line.split()
                                        ip = sp[0]
                                        ipsList.append(ip)
                        return ipsList
                else:
                        print("Enter a proper Location")
                print("-" * 40)
                print("Done")

        def get_dates(self):
                import os
                if os.path.isfile(self.location):
                        my_log_file_handle = open(self.location, "r")

                        list_of_lines = my_log_file_handle.readlines()

                        my_log_file_handle.close()

                        dateList = []
                        for my_each_line in list_of_lines:
                                sp = my_each_line.split()
                                for data in sp:
                                        if ((len(data) > 7) and (data[3] == "/" and data[7] == "/")):
                                                index_of_colon = data.index(':')
                                                dt = data[1:index_of_colon]
                                                dateList.append(dt)
                        return (dateList)
                else:
                        print("Enter a proper Location")
                print("-" * 40)
                print("Done")

        def get_pics(self):
                import os
                if os.path.isfile(self.location):
                        my_log_file_handle = open(self.location, "r")

                        list_of_lines = my_log_file_handle.readlines()

                        my_log_file_handle.close()

                        imageList = []
                        for my_each_line in list_of_lines:
                                sp = my_each_line.split()
                                for data in sp:
                                        if (data[len(data)-4:]==".jpg") or (data[len(data)-4:] == ".gif"):
                                                imageList.append(data[6:])
                        return (imageList)
                else:
                        print("Enter a proper Location")
                print("-" * 40)
                print("Done")

        def get_urls(self):
                import os
                if os.path.isfile(self.location):
                        my_log_file_handle = open(self.location, "r")

                        list_of_lines = my_log_file_handle.readlines()

                        my_log_file_handle.close()

                        ipsList = []
                        for my_each_line in list_of_lines:
                                sp = my_each_line.split()
                                for data in sp:
                                        if (data[1:12] == "http://www.")and len(data)>13:
                                                ipsList.append(data[1:len(data)-1])
                        return (ipsList)
                else:
                        print("Enter a proper Location")
                print("-" * 40)
                print("Done")


if __name__ == "__main__":
        object=Assignment7("../log/server_log.txt")
        print(object.get_ips())
        print(object.get_dates())
        print(object.get_pics())
        print(object.get_urls())