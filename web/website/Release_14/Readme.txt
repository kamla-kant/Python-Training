# Release_14
#################
# --------------
# Using Python web frameworks we can create
# 1) Website
# 2) RESTFul Web services (REST-API)
# 3) Micro Services
#
# In this section, We are creating
# 2) RESTFul Web services (REST-API)
# 3) Micro Services
# --------------

#################
# Changes in Release_14
#################
# - Copy of Release_13
# - Created Micro Service OR REST API for log data
#################

#################
# Scenario - 1 : REST API
#################
# - Suppose we need to give access to our logdata table with others
#
# Why to give our application access to others?
# Example : If google pay team ask Airtel to give access
#   so that google pay can collection bill payment .
#   then airtel will not say NO. Because airtel needs to increase the
#   business?
#   Many examples like we book PVR movie ticket in bookmyshow.com,
#   we can pay electrcity bill in google/phone pe etc
#
# - Finally to increase the business we need to give access
#
# How to give?
# OPTION - 1 : We can give mongodb /sql db credentials
#   like host, port, user, password, db name
# then others can get all data like using
# import pymysql
# con = pymysql.connect(user, pass, host, port, db)
#
# OPTION-1 is Not secured, we can't share our credentials
#
# Then how?
#
# we got 2 solutions (Without providing creadentials we can share)
# 1) SOAP : Simple Object Access Protocol Architecture/Design
# 2) REST : Representational State Transfer Architecture/Design
#
# Both architecture tells, dont provide credentials like mentioned
# in option-1
# instead, introduce some interface/gate between our application
# and others
# our db/application   --- GATE --->  Others
# our db/application   --- INTERFACE --->  Others
# our db/application   --- APPLICATION PROGRAMMING INTERFACE(API) --->  Others
#
# Flask framework implement REST architecture
# our db/application   --- REST API - APPLICATION PROGRAMMING INTERFACE(API) --->  Others
# REST API or RESTFul web services
#################

#################
# REST API & MICRO SERVICE - PART - 1
#################
# REST API is developed for others means, other person/ other application / other team / public
# Example : weather API we have seen now
#
# Other Scenario,
# in my own application, i may need to enable / disable some
# features of my application.
#
# Ex-1: Amazon.com : During summer he may need to enable summer tab
#   during winter he may need to disable summer and enable winter
#   tab.
# PROBLEM : making changes in the website will impact on the service
#   again it is difficult as well, because our changes may impact
#   other part of application.
#
# We wanted some solutin?
# We MiCro Service Architecture.
# Whichever part of our application, we want to run independently,
# we can create microservice and run independently
#
# Since it is running independently, whenever we want we can run the
#   service, and we can stop whenever we want.
# This will not impact on our main application.
#################

# REST API & MICRO SERVICE - PART - 2
#################
# How to REST API & MICRO SERVICE ?
# Both are same
#
# What is the difference?
# API -> is used by others
# Microservice -> will be our application
#################

# How to create REST API?
#################
# Steps :
# Step - 1 : Create END POINT
# Step - 2 : Return data in json
# Step - 3 : Run the server
#################
