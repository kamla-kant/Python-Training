"""
Using pytest,
test Assignemnt_4.
Test cases:
1) Atleaset one IP "123.123.123.123" present
2) Count of dates should greater than 2
3) Atleast one date should contain "Apr"
"""
def test_Atleast_one_IP_is_Present():
    from Assignment_4 import extract_IPs as exIps
    outcome=exIps("../log/server_log.txt")
    assert len(outcome) > 0

def test_count_of_dates_greater_than_2():
    from Assignment_4 import extract_Dates as exDt
    outcome = exDt("../log/server_log.txt")
    assert len(outcome) > 2

def test_dates_must_contain_Apr():
    from Assignment_4 import extract_Dates as exDt
    dateList = exDt("../log/server_log.txt")
    outcome=False
    for each in dateList:
        time=each.split("/")
        if(time[1]=="Apr"):
            outcome = True
            break
    assert outcome == True