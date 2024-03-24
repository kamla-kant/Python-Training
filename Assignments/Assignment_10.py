"""
Using pytest,
test Assignemnt_7.
Test cases:
1) Atleaset one image 'wpaper.gif' present
2) .gif files Count should be equal to 3
3) All urls should startswith 'http'
"""

def test_atleast_one_wrapper_image_present():
    from Assignment_7 import Assignment7
    assign7=Assignment7("../log/server_log.txt")
    output=assign7.get_pics()
    print(output)
    assert output.count("wpaper.gif")>0

def test_count_of_gif_is_3():
    from Assignment_7 import Assignment7
    assign7 = Assignment7("../log/server_log.txt")
    output = assign7.get_pics()
    count=0
    for each in output:
        if(each[len(each)-4:]==".gif"):
            count=count+1
    assert count==3

def test_all_url_start_with_http():
    from Assignment_7 import Assignment7
    assign7 = Assignment7("../log/server_log.txt")
    output = assign7.get_urls()
    ifhttps=True
    for each in output:
        if(each[0:4]!="http"):
            ifhttps=False
    assert ifhttps