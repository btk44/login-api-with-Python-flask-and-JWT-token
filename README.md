## About the project

This is just an example of using JWT token in Python flask API. 

### Built with

* flask
* JWT token
* MySQL database

## Requirements

    pip install Flask SimpleJSON PyJWT flask-sqlalchemy mysqlclient
    pip install -U flask-cors

## Short files description

* Code that performs all authorization actions is in api/auth
* The rest of api endpoints should go to api/api to keep auth nicely separated
* base directory is for base classes
* common directory holds all app settings
* tools directory holds mappers json<->dto (camel case to snake case) and dto<->db model 

## How to run:

1. Run Database creation.sql script to create example database loginappdb with test account (test/password)
2. Go to api/common/appsettings.py and change database connection string to match your user and password
3. Run code in Visual Studio Code

## VS Code setup

1. Open terminal and run:
```sh
cd api
python3 -m venv venv
source venv/bin/activate
pip install Flask SimpleJSON PyJWT flask-sqlalchemy mysqlclient
pip install -U flask-cors
```
2. Press ctrl+shift+P and write "interperter" -> choose Select Python Interpreter and find select path to api/venv/bin/python3
3. Go to Run and Debug tab (left sidebar) and click 'create a launch.json file'. Pick Python then Flask and input 'api/app.py' path. Hit Enter.
4. Run with F5

## Make requests

Use postman or whatever you like to make requests below:

### Login
   Make POST:
   ```sh
   http://localhost:5000/auth/login
   ```
   with body:
   ```sh
   {
      "accountName": "test",
      "password": "password"
   }
   ```

### Refresh
   Make POST:
   ```sh
   http://localhost:5000/auth/refresh
   ```
   with body:
   ```sh
   {
      "accountId": 1,
      "refreshToken": "PASTE YOUR REFRESH TOKEN HERE (LOGIN RESPONSE)"
   }
   ```

### Private endpoint
   Make GET:
   ```sh
   http://localhost:5000/test/private
   ```
   Don't forget to add token to headers!