'''
Refer Readme.txt
'''

import flask

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
    try:
        import sqlite3

        print("Connect/Creating database 'all_courses_db.sqlite3' ")
        all_courses_connection = sqlite3.connect('all_courses_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        all_courses_cursor = all_courses_connection.cursor()
        print("Done")

        all_courses_query = "SELECT * FROM ALL_COURSES"
        print("Executing Query : ", all_courses_query)
        all_courses_cursor.execute(all_courses_query)
        print("Done")

        print("Reading all data from cursor")
        all_courses_result = all_courses_cursor.fetchall()
        print("Done")

        return flask.render_template('about.html', all_courses=all_courses_result)

    except Exception as e:
        print("e : ", e)
        # If table not present then error
        # also any other error as well
        return "Add courses to our Portal <a href='/addcourse'>Click here to create course</a>"
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
            return "<h1>Account Created Successfully <a href='/login'>Goto Login</a></h1>"
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
            flask.session['username'] = entered_username
            # return "Login Success <a href='/'>Go To Home Page</a>"
            return flask.redirect("/about")
        else:
            return "Login Failed (Wrong Credentials) <a href='/login'>Goto Login</a>"

    except Exception as e:
        print("e : ", e )
        # If table not present then error
        # also any other error as well
        return "Check whether you created the account <a href='/createaccount'>Create Account</a>"
# ------------

# ------------

# ------------

# ------------
# END POINT - 9 : http://127.0.0.1:5000/createaccount
# ------------
@my_website_app.route('/addcourse')
def create_course_page():
    return flask.render_template('add_course.html')
# ------------

# END POINT - 10 : http://127.0.0.1:5000/addnewcourse
# ------------
@my_website_app.route('/addnewcourse', methods=['POST'])
def create_course():
    entered_title = flask.request.form.get('tit')
    entered_description = flask.request.form.get('des')
    entered_prerequisites = flask.request.form.get('pre')
    entered_learnings = flask.request.form.get('lrn')
    entered_duration = flask.request.form.get('dur')
    entered_creator = flask.request.form.get('nam')

    import sqlite3

    print("Connect/Creating database 'all_courses_db.sqlite3' ")
    all_courses_connection = sqlite3.connect('all_courses_db.sqlite3')
    print("Done")

    print("Get the cursor.(It help us to send query & retreive result)")
    all_courses_cursor = all_courses_connection.cursor()
    print("Done")

    print("Create a table if not exists")
    all_courses_query = '''
            CREATE TABLE IF NOT EXISTS ALL_COURSES(
            TITLE VARCHAR(100),
            DESCRIPTION VARCHAR(100),
            PREREQUISITE VARCHAR(100),
            LEARNINGS VARCHAR(100),
            DURATION VARCHAR(100),
            CREATOR VARCHAR(100),
            ENROLLED VARCHAR(100)
            )
            '''

    print("Executing Query : ", all_courses_query)
    all_courses_cursor.execute(all_courses_query)
    print("Done")

    # Insert into table
    all_courses_query = f"INSERT INTO ALL_COURSES VALUES('{entered_title}', '{entered_description}', '{entered_prerequisites}','{entered_learnings}', '{entered_duration}', '{entered_creator}','{0}')"
    print("Executing Query : ", all_courses_query)
    all_courses_cursor.execute(all_courses_query)
    print("Done")

    all_courses_connection.commit()
    print("User account created")
    print("Closing DB")
    all_courses_connection.close()
    print("Done")
    return "<h1>Course Added Successfully. Thank You <a href='/about'>Goto Courses</a></h1>"

# END POINT - 11 : http://127.0.0.1:5000/register
# ------------
@my_website_app.route('/register/<course>')
def register_course_page(course):
    u = flask.session.get('username')
    if u is None:  # Not logged in
        return "<h1>Login first to Register <a href='/login'>Goto Login</a></h1>"
    else:
        import sqlite3

        print("Connect/Creating database 'all_courses_db.sqlite3' ")
        all_courses_connection = sqlite3.connect('all_courses_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        all_courses_cursor = all_courses_connection.cursor()
        print("Done")

        all_courses_query = f"SELECT * FROM ALL_COURSES WHERE TITLE ='{course}'"
        print("Executing Query : ", all_courses_query)
        all_courses_cursor.execute(all_courses_query)
        print("Done")

        print("Reading all data from cursor")
        course_result = all_courses_cursor.fetchall()
        print("Done")

        return flask.render_template('register.html', course=course_result)
# ------------

# END POINT - 11 : http://127.0.0.1:5000/logout
# ------------
@my_website_app.route("/logout", methods=["GET"])
def my_logout_page():
    del flask.session["username"]
    return "<h1>Logout Success <a href='/login'>Go Back</a></h1>"

# ------------

# END POINT - 12 : http://127.0.0.1:5000/registration
# ------------
@my_website_app.route("/registration/<course>/<enrolled>", methods=["POST","GET"])
def registration_action(course, enrolled):
    import sqlite3

    print("Connect/Creating database 'enrolled_courses_db.sqlite3' ")
    enrolled_courses_connection = sqlite3.connect('enrolled_courses_db.sqlite3')
    print("Done")

    print("Get the cursor.(It help us to send query & retreive result)")
    enrolled_courses_cursor = enrolled_courses_connection.cursor()
    print("Done")

    print("Create a table if not exists")
    enrolled_courses_query = '''
                CREATE TABLE IF NOT EXISTS ENROLLED_COURSES(
                NAME VARCHAR(100),
                COURSE VARCHAR(100)
                )
                '''

    print("Executing Query : ", enrolled_courses_query)
    enrolled_courses_cursor.execute(enrolled_courses_query)
    print("Done")
    enrolled_courses_query = f"SELECT NAME FROM ENROLLED_COURSES WHERE NAME='{flask.session.get('username')}' AND COURSE='{course}'"
    print("Check if relation already exists")
    print("Executing Query : ", enrolled_courses_query)
    enrolled_courses_cursor.execute(enrolled_courses_query)
    print("Check if relation already exists")
    enrolled_courses_result = enrolled_courses_cursor.fetchall()
    print(enrolled_courses_result)
    if len(enrolled_courses_result) == 0:

        print("Connect/Creating database 'all_courses_db.sqlite3' ")
        all_courses_connection = sqlite3.connect('all_courses_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        all_courses_cursor = all_courses_connection.cursor()
        print("Done")

        all_courses_query = f"UPDATE ALL_COURSES SET ENROLLED = '{str(int(enrolled) + 1)}' WHERE TITLE ='{course}'"
        print("Executing Query : ", all_courses_query)
        all_courses_cursor.execute(all_courses_query)
        print("Done")

        all_courses_connection.commit()
        print("User account created")
        print("Closing DB")
        all_courses_connection.close()
        print("Done")
        print(flask.session.get('username'))

        # Insert into table
        enrolled_courses_query = f"INSERT INTO ENROLLED_COURSES VALUES('{flask.session.get('username')}', '{course}')"
        print("Executing Query : ", enrolled_courses_query)
        enrolled_courses_cursor.execute(enrolled_courses_query)
        print("Done")

        enrolled_courses_connection.commit()
        print("User account created")
        print("Closing DB")
        enrolled_courses_connection.close()
        print("Done")

        return "<h1>Successfully Registered to Course. Thank You <a href='/about'>Goto Courses</a></h1>"
    else:
        return "<h1>You have Already Registered to Course. Please Check <a href='/about'>Goto Courses</a></h1>"



# ------------

# ------------
# END POINT - 13 : http://127.0.0.1:5000/registered_courses
# ------------
@my_website_app.route('/registered_courses')
def enrolled_courses_page():
    try:
        import sqlite3


        print("Connect/Creating database 'enrolled_courses_db.sqlite3' ")
        enrolled_courses_connection = sqlite3.connect('enrolled_courses_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        enrolled_courses_cursor = enrolled_courses_connection.cursor()
        print("Done")
        enrolled_courses_query = f"SELECT * FROM ENROLLED_COURSES WHERE NAME = '{flask.session.get('username')}'"
        print("Executing Query : ", enrolled_courses_query)
        enrolled_courses_cursor.execute(enrolled_courses_query)
        enrolled_courses_result = enrolled_courses_cursor.fetchall()
        print("Done")
        if len(enrolled_courses_result)>0:
            return flask.render_template('registered_courses.html', enrolled_courses=enrolled_courses_result)
        else:
            return "<h1>You have not Enrolled in any course <a href='/about'>Navigate to Courses</a></h1>"


    except Exception as e:
        print("e : ", e)
        # If table not present then error
        # also any other error as well
        return "<h1>You have not Enrolled in any course <a href='/about'>Navigate to Courses</a></h1>"

# ------------
# Run Web Server
# ------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# ------------
