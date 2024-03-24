# MongoDB
 ######################

 # POINT - 1
 # --------------------
 # We have many kinds of websites we visit everyday
 # example : google.com, facebook.com, icicibank.com etc
 # --------------------

 # POINT - 2
 # --------------------
 # Few websites activity are in the control of website owner.
 #   Example : icicibank.com
 #
 # Few websites activity are in the control of customers like us.
 #   Example : facebook.com, slack etc
 # --------------------

 # POINT - 3
 # --------------------
 # In case of icicibank.com, bank owner will design website and give access to
 #   customers. Customers will use the options avaiable in their website
 #
 # In case of facebook.com, facebook owner gave control to customer on
 # - Creating how much ever post you want
 # - Creating how much group you want
 # Many more option they are given to customer
 #
 # In case of slack also,
 #   - I can add n numbers of groups
 #   - I can create n numbers of channels
 #   - In each channel, i can add n number of participants
 #   Many other options as well
 # --------------------
 # POINT - 4
 # --------------------
 # In Databases we have 2 types of databases
 # 1) : SQL Databases where we are storing in 'tables' and communicate using SQL queries
 # 2) : No-SQL Databases where we are storing in json format. NOT USING SQL to communicate
 # --------------------

 # POINT - 5
 # --------------------
 # - In case of websites like icicibank, college website, company website example, SQL databases will be used
 # - In case of facebook, slack etc kind of examples, No-SQL databases will be used.
 #
 # Why?
 # In case facebook, slack etc where we dont have control on how many
 # tables we need to create/delete/update etc when they are adding/removing/updating groups
 # or channels etc
 # Means, dynamically creating tables/deleting tables will lead to
 # consuming more resources in case of SQL databases
 # Because of this reason,
 # we got no-sql databases
 # --------------------
 # POINT - 6
 # --------------------
 # In python,
 # we have library like 'pymongo' to communicate with mongoDB
 # python program   <--Communicate using (pymongo)--> mongoDB
 #
 # So,
 # We need to install
 # 1) mongoDB
 # 2) pymongo
 # --------------------

 # POINT - 7 : mongoDB without python program
 # --------------------
 # Download & Install mongoDB and communicate without
 # using python program
 #
 # We can download from : https://www.mongodb.com/try/download/community
 #
 # --------------------
 # POINT - 8 (PART-1): mongoDB without python program
 # --------------------
 # Steps to communicate with mongodb without python program
 #
 # Step - 1 : Start MongoDB server in ONE TERMINAL / CMD PROMPT

 # RUN THIS COMMAND TO RUN THE SERVER in mongodb server 'bin' dir
 #       Command : mongod
 # Example : C:\MyInstall\mongodb-win32-x86_64-windows-5.0.4\bin>mongod
 #
 # MINIMIZE THE TERMINAL, DONT CLOSE
 # --------------------
 # POINT - 8 (PART-2): mongoDB without python program
 # --------------------
 # Step - 2 : Open Another terminal/cmd prompt then run mongodb client
 #   through the client, we can communicate to mongodb.
 #  Command : mongo
 # Example : C:\MyInstall\mongodb-win32-x86_64-windows-5.0.4\bin>mongo
 # --------------------
 # POINT - 8 (PART-3): mongoDB without python program
 # --------------------
 # Steps to communicate through mongo clietn
 #
 # Step - 1 : First list all databases
 #   Commands : show dbs
 #
 # Step - 2 : Create database
 #   Commands : use mytestdb1
 #
 # Step - 3 : Show current database
 #   Commands : db
 #
 # Step - 4 : Show all collections (In SQL we will use tables)
 #   Commands : show collections
 #
 # Step - 5 : Create new collection
 #   Commands : db.createCollection("MyCollection1")
 #
 # Step - 6 : Show all collections (In SQL we will use tables)
 #   Commands : show collections
 #
 # Step - 7 : Insert data - pass in the form of dictionary
 #   Commands : db.MyCollection1({"A":10})
 #
 # Step - 8 : Read data from collection
 #   Commands : db.MyCollection1.find()
 #
 # Step - 9 : Close the db
 #   Commands : db.close
 # --------------------