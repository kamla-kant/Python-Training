# How to create session?
####################
# Step - 1) install flask-session
# Step - 2) from flask import session
# Step - 3) my_website_app.secret_key = "MySecreteKey123"
# Step - 4) in /validatelogin ENDPOINT
#           # flask.session['userloggedin'] = "yes"
#            session['username'] = entered_username
#
# DONE : SESSION CREATED
####################

# How to know in report tab if user logged in ?
####################
# Step - 1 : u = session.get('username')
# Step - 2 : if u is None then not logged in and redirect to /login
# Step - 3 : if u is not None then get all log data from db and send to logreport.html
####################

# How to display in logreport.html?
####################
