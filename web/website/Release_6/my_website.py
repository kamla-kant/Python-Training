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

# Run Web Server
# ------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# ------------