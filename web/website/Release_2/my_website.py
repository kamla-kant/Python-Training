'''
 Refer Readme.txt
 HANDLING ERROR
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

# Run Web Server
# ------------
my_website_app.run()
# my_website_app.run(host='127.0.0.1', port=1234)
# ------------