"""
 from below string, extract
 IP
 DATE
 PICS
 URL
 from each line which is starting with IP adress
 """

log_data = '''
 The following is a fragment from the server logs for JafSoft Limited. All the relative URLs are for the base URL http://www.jafsoft.com/.

 First lets look at a fragment of log file....

 fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
 fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

 ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
 123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
 123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
 123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
 123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
 123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

 (Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

 The fragment shown represents three visitors to my web site
 '''

print("log data :")
print("-" * 40)
# -------------------

print(log_data)

print("-" * 40)
# -------------------

print("type of log data :")
print("-" * 20)
# -------------------

print(type(log_data))

print("-" * 40)
# -------------------

# print will display where \n will be replaced with newline
# \t will be replacted with tab space etc.
# BUT
# if we display in raw format then we may get idea of how to
# extract

print("log data in raw format :")
print("-" * 20)
# -------------------

print(repr(log_data))

print("-" * 20)
# -------------------

# As per requirements,
# we need to traverse each line and
# check whether it is IP address
# if yes then extract
# else go for next line

# Now some how if we get list of lines then
# we can do something

# split by \n to get list of lines

print("Get list of lines")
print("-" * 40)
# ----------------

list_of_lines = log_data.split("\n")
print(list_of_lines)

print("-" * 40)
# ----------------

# Now what next?
# we need to traverse each line and
# check whether it is IP address
#   - check if first 3 chars are digit then treat/ASSUME it is IP line
#   - OR 2nd option is writing REGULAR EXPRESSION
# if yes then extract
# else go for next line

for my_each_line in list_of_lines:
    first_three_chars = my_each_line[1:4]
    if first_three_chars.isdigit():
        # Below code is copied from example :-6
        print("Extracting Info")
        print("-" * 40)
        # --------------------
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

        print(ip, dt, im, url)

        print("-" * 40)
        # --------------------