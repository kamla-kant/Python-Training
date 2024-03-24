# Release_12
#################
# --------------
# Using Python web frameworks we can create
# 1) Website
# 2) RESTFul Web services (REST-API)
# 3) Micro Services
#
# In this section, We are creating
# 1) website
# --------------

#################
# Changes in Release_12
#################
# - Copy of Release_11
# - If we click on 'Report' tab
#   then if user logged in then display Log data from db
#   if not logged in then redirect to login page
#################

# HOW TO KNOW whether user is logged in or not?
#################
# - If it is in same login function then we will be knowing user logged in
# if credentials are correct else not logged in
# - But we need to know whether user logged in or not in different pages/tabs/request
#   thenhow?
# - we have seesion object provided for this purpose
# - install flask-session
#################

# Steps to use session in flask
#################
# Step - 1 : add secrete key : this key will be used during the session
# my_website_app.secret_key = "MySecreteKey123"
#
# Step - 2 : Whenever we want to store some data/flag then use session object
# flask.session['userloggedin'] = "yes"
#
# Step - 3 : Whenever you want to know, user logged in then
#   status = flask.session.get('userloggedin')
#   if None then user is not logged in else user is logged in.
#################

# Our Requrement:
# # - If we click on 'Report' tab
#   then if user logged in then display Log data from db
#   if not logged in then redirect to login page
#############################
# Step - 1 : add secret_key
#
# Step - 2 : Once we log in , it will goto /validatelogin
#       so created
#       flask.session['username'] = entered_username
#
# Step - 3 : If login success then redirect to /report
#
# Step - 4 : Write ENDPOINT for /report
#############################

# Add logout
################
# - if login then only display logout button
#   my_template.html
