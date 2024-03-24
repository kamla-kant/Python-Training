"""
 This is developed for testing purpose
 This is developed to test project_1.py

 Requirement given by client:
 1. add of 10 & 20 should be 30
 2. sub of 10-20 should be -10
 3. add of 'Hello' and 'Python' should be 'HelloPython'
 4. add of -10 & -20 should not be -10
 5. sub of 10-30 should not be 20

 we need to test whether all the cases
 are working
 """

'''
- each test case write one function
- each function name should be starting with test_functionname
- file name also should starts with test_filename.py
'''


# 1. add of 10 & 20 should be 30
def test_case_1():
    from project_1 import add, sub
    result = add(10, 20)
    assert result == 30  # True means No Error, False Means AssertionError
    # If AssertionError the pytest framework will consider test case failed


# 2. sub of 10-20 should be -10
def test_case_2():
    from project_1 import add, sub
    result = sub(10, 20)
    assert result == -10


# 3. add of 'Hello' and 'Python' should be 'HelloPython'
def test_case_3():
    from project_1 import add, sub
    result = add('Hello', 'Python')
    assert result == 'HelloPython'


# 4. add of -10 & -20 should not be -10
def test_case_4():
    from project_1 import add, sub
    result = add(-10, -20)
    assert result != -10


# 5. sub of 10-30 should not be 20
def test_case_5():
    from project_1 import add, sub
    result = sub(10, 30)
    assert result != 20

# How to Run ?
# 2 ways
# 1 way - install pycharm plugin and right click and run in pytest
# 2 way - command prompt
#   COMMAND : python -m pytest -v test_project_1.py
# OR
#   COMMAND : pytest test_project_1.py
# OR
#   COMMAND : python -m pytest -v
# (Above command will run all the files which is starting with test_filename.py)