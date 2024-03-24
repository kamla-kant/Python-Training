'''
 Refer Readme.txt
 '''

import flask

# Create App for our website
# ------------
my_website_app = flask.Flask(__name__)
# ------------

# ------------
# Handle 404 error
# ------------


@my_website_app.errorhandler(404)
def my_404_error_page(error):
    return "Page Under Construction"
# ------------

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
        from pymongo import MongoClient

        print("Connecting mongo db server")
        mongodb_connection = MongoClient(host='127.0.0.1', port=27017)
        print("Done")

        db = mongodb_connection['students_db']
        print("Done")

        print("Creating/Connecting to collection 'student_table'")
        students_collection = db["students_table"]
        print("Done")

        # ------------------------

        # ------------------------
        # Check Whether username already exists
        # ------------------------
        my_db_result = students_collection.find()
        print(my_db_result)
        print("Check Whether username already exists")
        for each_record in my_db_result:
            if (each_record["USER_NAME"]==entered_username):
                return "Username already Created Exists <a href='/login'>Goto Login</a>"


        print("Username Doesn't exists. Proceeding to account creation")
        # ------------------------

        # ------------------------
        # Create Account
        # ------------------------
        # Insert into table
        students_data = {"USER_NAME": entered_username, "PASSWORD": entered_password_1, "EMAIL": entered_email}
        print(f"Inserting data {students_data}")
        students_collection.insert_one(students_data)
        print("Done")
        print("User account created")
        print("Closing DB")
        mongodb_connection.close()
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
        from pymongo import MongoClient

        print("Connecting mongo db server")
        mongodb_connection = MongoClient(host='127.0.0.1', port=27017)
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        my_db_cursor = my_db_connection.cursor()
        print("Done")

        db = mongodb_connection['students_db']
        print("Done")

        print("Creating/Connecting to collection 'student_table'")
        students_collection = db["students_table"]
        print("Done")

        my_db_result = students_collection.find()
        print("Check Whether username already exists")
        valid = False
        for each_record in my_db_result:
            if (each_record["NAME"] == entered_username and each_record["PASSWORD"]==entered_password):
                valid = True
                print("Valid Credentials")
                return "Login Success <a href='/'>Go To Home Page</a>"
        if(not valid):
            print("Not valid credentials")
            return "Login Failed (Wrong Credentials) <a href='/login'>Goto Login</a>"

    except:
        # If table not present then error
        # also any other error as well
        return "Check whether you created the account <a href='/createaccount'>Create Account</a>"


# ------------

# Run Web Server
# ------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# ------------

