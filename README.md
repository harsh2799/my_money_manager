# my_money_manager
A simple money managing website with functionality to split the bill among peers accurately and conviniently.

# Folder Structure:

MY_MONEY_MANAGER
----------------
```
My_Money_Manager
|- client [For the Front End - React]
    |---- public [Contains public assets.]
    |---- src
            |---- components [contains .jsx files for all components.]
            |---- pages [contains .jsx files for all pages.]
            |---- App.js [file to load all pages]
            |---- injex.js [file to load App.js]
|- server [For the Backend - Flask, FlaskRestful, MongoDb]
    |
    |---- app
            |---- model [Contains files for Database operations.]
            |---- service [Contains all service files for the backend process.]
            |---- resources.py [Contains all the resource classes with get and post function and connects them with respective service class.]
            |---- routes.py [Contains all the routes for backend and connects them to respective resource class.]
            |---- __init__.py [Init file for the app.]
    |---- config.py [Contains all the configuration required for the project.]
    |---- config.json [Json file to contain all the Configuration in json format.]
    |---- run.py [To run the server]
```

# Commands:

- To Run Client: cd client -> npm start client
- To install Virtual Environment -> python -m venv venv
- To activate Virtual Environment -> cd server -> ./venv/Scripts/activate.bat or ./venv/Scripts/activate
- To install requirements -> pip install -r requirements.txt
- To Run Server: cd server -> python run.py

# Features [To be Added]:
```
[] - User Able to Create Account
[] - User Able to Sign In
    - Google Sign-In?
[] - User Able to add Initial Money to Spend in the month.
    - Credit and Debit based functionality
[] - User able to create various categories he spents money on. [Bills, Rent, Food, Entertainment etc.]
[] - Dashboard showing current spent and money available with categories and amount spent on each category/ amount available for each category.
[] - Inside each category list of items money spent on - Datewise [Name - Amount]
[] - Past Data with list of amount set vs spent and then detailed view of each month.
[] - Statistics to show most money spent on etc [We can figure it out].
[] - Backup data to users google drive?
    - similar to whatsapp backups? (We can figure it out)
```