"""
This is REST API developed to expose
all Course data in json format
"""
# ------------
import flask
my_rest_api_app = flask.Flask("MyAPIApp")
# ------------

# ------------
# REST API or MICRO SERVICE END POINT : http://127.0.0.1:6060/addcourses
# ------------
@my_rest_api_app.route("/addcourses", methods=["GET"])
def my_rest_api_app_addcourses():
        import sqlite3

        print("Connect/Creating database 'all_courses_db.sqlite3' ")
        my_db_connection = sqlite3.connect('all_courses_db.sqlite3')
        print("Done")

        print("Get the cursor.(It help us to send query & retreive result)")
        my_db_cursor = my_db_connection.cursor()
        print("Done")

        my_query = "SELECT * FROM ALL_COURSES"
        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        print("Done")

        print("Reading all data from cursor")
        my_db_result = my_db_cursor.fetchall()
        print("Done")

        return flask.jsonify(my_db_result)
# ------------


# ------------
# Run the server
# ------------
my_rest_api_app.run(port=6060)
# ------------
