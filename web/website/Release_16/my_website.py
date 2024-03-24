'''
Refer Readme.txt
'''

import flask
from flask import session
# Create App for our website
# ------------
my_website_app = flask.Flask(__name__)
my_website_app.secret_key = "MySecreteKey123"
# ------------

# ------------
# Handle 404 error
# ------------
@my_website_app.errorhandler(404)
def my_404_error_page(error):
    return "Page Under Construction"
# ------------
#
# # ------------
# # END POINT - 1 : http://127.0.0.1:5000/
# # ------------
# @my_website_app.route('/') # '/' is mapped to url http://127.0.0.1:5000/
# def my_home_page():
#     return "Wel Come"
# # ------------

# ------------
# END POINT - 2 : http://127.0.0.1:5000/
# ------------
@my_website_app.route('/')
def my_home_page():
    return flask.render_template('home.html')
# ------------

# ------------
# END POINT - 3 : http://127.0.0.1:5000/about
# ------------
@my_website_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# ------------

# ------------
# END POINT - 4 : http://127.0.0.1:5000/login
# ------------
@my_website_app.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# ------------

# ------------
# END POINT - 5 : http://127.0.0.1:5000/createaccount
# ------------
@my_website_app.route('/createaccount')
def my_createaccount_page():
    return flask.render_template('newuser.html')
# ------------

# ------------
# END POINT - 6 : http://127.0.0.1:5000/addnewuser
# ------------
@my_website_app.route('/addnewuser', methods=['POST'])
def my_addnewuser_page():
    # Whatever the data we are entering in front end,
    # all the data will be captured by framework
    # and stored in 'flask.request.form' variable in the
    # form of dictionary
    # flask.request.form = {'uname':'entered data', 'pw1': 'entered data' } etc
    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('pw1')
    entered_password_2 = flask.request.form.get('pw2')
    entered_email = flask.request.form.get('email')

    if entered_password_1 != entered_password_2:
        return "Password didn't match <a href='/createaccount'>Go Back</a>"
    else:
        # Store data in database

        # ------------------------
        # Connect to DB and create table if not exists
        # ------------------------
        import sqlite3

        print("Connect/Creating database 'my_website_db.sqlite3' ")
        my_db_connection = sqlite3.connect('my_website_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        my_db_cursor = my_db_connection.cursor()
        print("Done")

        print("Create a table if not exists")
        my_query = '''
        CREATE TABLE IF NOT EXISTS MYUSERS(
        NAME VARCHAR(100),
        PASSWORD VARCHAR(100),
        EMAIL VARCHAR(100)
        )
        '''

        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        print("Done")
        # ------------------------

        # ------------------------
        # Check Whether username already exists
        # ------------------------
        my_query = f"SELECT NAME FROM MYUSERS WHERE NAME='{entered_username}' AND PASSWORD='{entered_password_1}'"
        print("Check Whether username already exists")
        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        my_db_result = my_db_cursor.fetchall()
        if len(my_db_result) > 0 : # Then user record found
            print("Username already exists")
            return "Username already exists <a href='/createaccount'>Go Back</a>"
        else:
            print("Username Doesn't exists. Proceeding to account creation")
            # ------------------------

            # ------------------------
            # Create Account
            # ------------------------
            # Insert into table
            my_query = f"INSERT INTO MYUSERS VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
            print("Executing Query : ", my_query)
            my_db_cursor.execute(my_query)
            print("Done")

            my_db_connection.commit()
            print("User account created")
            print("Closing DB")
            my_db_connection.close()
            print("Done")
            return "Account Created Successfully <a href='/login'>Goto Login</a>"
# ------------

# ------------
# END POINT - 7 : http://127.0.0.1:5000/validatelogin
# ------------
@my_website_app.route("/validatelogin", methods=["POST"])
def my_validate_login_page():
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    try:
        import sqlite3

        print("Connect/Creating database 'my_website_db.sqlite3' ")
        my_db_connection = sqlite3.connect('my_website_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        my_db_cursor = my_db_connection.cursor()
        print("Done")

        my_query = f"SELECT NAME FROM MYUSERS WHERE NAME='{entered_username}' AND PASSWORD='{entered_password}'"
        print("Check Whether username already exists")
        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        my_db_result = my_db_cursor.fetchall()

        if len(my_db_result) > 0 : # Then user record found
            print("Username already exists. So Login Success")
            # flask.session['userloggedin'] = "yes"
            session['username'] = entered_username
            # return "Login Success <a href='/'>Go To Home Page</a>"
            return flask.redirect("/report")
        else:
            return "Login Failed (Wrong Credentials) <a href='/login'>Goto Login</a>"

    except Exception as e:
        print("e : ", e )
        # If table not present then error
        # also any other error as well
        return "Check whether you created the account <a href='/createaccount'>Create Account</a>"
# ------------

# ------------
# END POINT - 8 : http://127.0.0.1:5000/report
# ------------
@my_website_app.route("/report", methods=["GET"])
def my_log_report_page():
    # If not loggeed in redirect to login page
    u = session.get('username')
    if u is None: # Not logged in
        return flask.redirect("/login")
    else: # if already logged in
        # query log data from db and display in table format
        import sqlite3

        print("Connect/Creating database 'my_db.sqlite3' ")
        my_db_connection = sqlite3.connect('my_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        my_db_cursor = my_db_connection.cursor()
        print("Done")

        my_query = "SELECT * FROM MYLOGDATA"
        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        print("Done")

        print("Reading all data from cursor")
        my_db_result = my_db_cursor.fetchall()
        print("Done")

        # we can send my_db_result to front end html
        # we can write python code to process this list in html
        # since html will be having its own code,
        #   we will write python code using below syntax
        #   1) {% any python statemnte %}
        #   2) {% if cond:%}
        #       {%endif%}
        #   3) {{variable_name}}
        #

        # How to display our data in html?
        # 1) display in table and green color
        #
        return flask.render_template("logreport.html", my_data=my_db_result)
# ------------


# ------------
# END POINT - 8 : http://127.0.0.1:5000/logout
# ------------
@my_website_app.route("/logout", methods=["GET"])
def my_logout_page():
    del session["username"]
    return "Logout Success <a href='/login'>Go Back</a>"
# ------------


# ------------
# END POINT - 9 : http://127.0.0.1:5000/restapi
# ------------
@my_website_app.route("/restapi", methods=["GET"])
def my_api_data():
    import requests
    my_rest_api_endpoint = "http://127.0.0.1:6060/logdata"
    try: # IF service is UP
        my_api_response = requests.get(my_rest_api_endpoint)
        my_api_response = my_api_response.json()
        print("my_api_response : ", my_api_response)
        return flask.render_template("logreport.html", my_data=my_api_response)
    except: # IF SERVICE IS DOWN
        return flask.render_template("servicedown.html")


# ------------
# Run Web Server
# ------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# ------------
