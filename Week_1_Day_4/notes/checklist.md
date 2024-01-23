# Checklist

1. create a new folder
2. go into the folder
3. open up a terminal in that location
   ```
   pipenv install flask 
   ```
4. `WARNING` check for pipfile & pipfile.lock
5. launch venv 
   ```
   pipenv shell
   ```
6. create my file structure
   1. Root folder (name of my project)
      1. flask_app
         1. config 📁
            1. mysqlconnection.py 📄
         2. controllers 📁
            1. controller_animal.py 📄
         3. models 📁
            1. model_animal.py 📄
         4. static📁
            1. css 📁
               1. style.css 📄
            2. js 📁
               1. script.js 📄
         5. templates 📁
            1. index.html 📄
         6. \_\_init__.py 📄
      2. pipfile 📄
      3. pipfile.lock 📄 
      4. server.py 📄
7. add boilerplate code
8. Test to make sure server is working


# My File boilerplates

## \_\_init__.py
```py
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "Nobody will know, how would they know?"

bcrypt = Bcrypt(app)

DATABASE = "database name here"

```

## server.py
```py
from flask_app import app
from flask_app.controllers import controller_animal


if __name__=="__main__":    
    app.run(debug=True)   
```

## mysqlconnection.py
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = False)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("**********Something went wrong**********", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

## Model.py file
```py
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Game:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

      #   add additional columns here

    # CREATE
    @classmethod
    def create(cls, data:dict) -> int:
      #! #TODO change table_name to the table name && update the column names and values
        query = "INSERT INTO table_name (name, genre, rating, release_year, company) VALUES (%(name)s, %(genre)s, %(rating)s, %(release_year)s, %(company)s);"
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id

    # READ
    @classmethod
    def get_all(cls):
      #! #TODO change table_name to the table name
        query = "SELECT * FROM table_name;"
        results = connectToMySQL(DATABASE).query_db(query)

        if not results:
            return []

        instance_list = []
        for dict in results:
            instance_list.append( cls(dict) )
        return instance_list
    
    @classmethod
    def get_one(cls, data:dict):
        """
        the data dictionary needs a key of 'id'
        """
        #! #TODO change table_name to the table name
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if not results:
            return []
        
        # convert the 1st item in the list to an instance of the class
        dict = results[0]
        instance = cls(dict)
        return instance

    # UPDATE


    # DELETE
    @classmethod
    def delete_one(cls, data:dict):
        """
        the data dictionary needs a key of 'id'
        """
        #! #TODO change table_name to the table name
        query = "DELETE FROM table_name WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
```

## User model File 
```py
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re	# the regex module

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

      #   add additional columns here
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    # CREATE
    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)

        if not results:
            return []

        instance_list = []
        for dict in results:
            instance_list.append( cls(dict) )
        return instance_list
    
    @classmethod
    def get_one(cls, data:dict):
        """
        the data dictionary needs a key of 'id'
        """
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if not results:
            return []
        
        # convert the 1st item in the list to an instance of the class
        dict = results[0]
        instance = cls(dict)
        return instance
    
    @classmethod
    def get_one_by_email(cls, data:dict):
        """
        the data dictionary needs a key of 'email'
        """
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if not results:
            return []
        
        # convert the 1st item in the list to an instance of the class
        dict = results[0]
        instance = cls(dict)
        return instance

    # UPDATE


    # DELETE
    @classmethod
    def delete_one(cls, data:dict):
        """
        the data dictionary needs a key of 'id'
        """
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(data:dict) -> bool:
        is_valid = True

        if (len(data['first_name']) < 2):
            flash("first_name is required, must be 2 characters or more", "err_users_first_name")
            is_valid = False

        if (len(data['last_name']) < 2):
            flash("last_name is required, must be 2 characters or more", "err_users_last_name")
            is_valid = False

        if (len(data['email']) < 7):
            flash("email is required, must be 7 characters or more", "err_users_email")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "err_users_email")
            is_valid = False
        else:
            potential_user = User.get_one_by_email(data)
            if potential_user:
                flash("Email address already exists!", "err_users_email")
                is_valid = False

        if (len(data['password']) < 8):
            flash("password is required, must be 8 characters or more", "err_users_password")
            is_valid = False

        if (len(data['confirm_password']) < 8):
            flash("confirm_password is required, must be 8 characters or more", "err_users_confirm_password")
            is_valid = False

        elif data['password'] != data["confirm_password"]:
            flash("Password and Confirm Password do not match", "err_users_confirm_password")
            is_valid = False

        return is_valid
    
    @staticmethod
    def validate_login(data:dict) -> bool:
        is_valid = True

        if (len(data['email']) < 7):
            flash("email is required, must be 7 characters or more", "err_users_email_login")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "err_users_email_login")
            is_valid = False
        else:
            potential_user = User.get_one_by_email(data)
            if not potential_user:
                flash("Invalid Credentials!", "err_users_password_login")
                is_valid = False

        if (len(data['password']) < 8):
            flash("password is required, must be 8 characters or more", "err_users_password_login")
            is_valid = False
        
        if is_valid:
            if not bcrypt.check_password_hash(potential_user.password, data['password']):
                flash("Invalid Credentials!", "err_users_password_login")
                is_valid = False
            else:
                session['uuid'] = potential_user.id

        return is_valid
```

## controller.py
```py
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_game import Game

# DISPLAY ROUTE -> Shows the form to create a game
@app.route('/game/new')
def game_new():
    return render_template('game_new.html')

# ACTION ROUTE -> process the form from the new route (above)
@app.post('/game/create')
def game_create():
    #TODO do the logic for creating the row in the database here. 
    return redirect('/')

# DISPLAY ROUTE -> just display the game info
@app.route('/game/<int:id>')
def game_show(id):
    #TODO get the game from the database and pass that instance of the game to the html page
    return render_template('game_show.html')

# DISPLAY ROUTE -> display the form to edit the game
@app.route('/game/<int:id>/edit')
def game_edit(id):
    #! #TODO in the future make sure that the user is suppose be able to update the record. 

    #TODO get the game from the database and pass that instance of the game to the html page
    return render_template('game_edit.html')

# ACTION ROUTE -> process the form from the edit route
@app.post('/game/<int:id>/update')
def game_update(id):
    #! #TODO in the future make sure that the user is suppose be able to update the record. 

    #TODO using the id that comes in update the record 
    return redirect('/')

# ACTION ROUTE -> delete the record from the database
@app.post('/game/<int:id>/delete')
def game_delete(id):
    #! #TODO in the future make sure that the user is suppose be able to update the record. 

    #TODO call on the delete method from the class to delete the row in the database
    return redirect('/')
```


# Form Templates

## Login
```html
<div>
        <h2>Login</h2>
        <form action="/users/login/process" method="post">
            <div>
                <label for="email">email</label>
                <input type="text" name="email" id="email">
                {% for message in get_flashed_messages(category_filter=['err_users_email_login']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <div>
                <label for="password">password</label>
                <input type="text" name="password" id="password">
                {% for message in get_flashed_messages(category_filter=['err_users_password_login']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <button>Login</button>
        </form>
    </div>
```

## Register
```html
<div>
        <h2>Register</h2>
        <form action="/users/create" method="post">
            <div>
                <label for="first_name">first_name</label>
                <input type="text" name="first_name" id="first_name">
                {% for message in get_flashed_messages(category_filter=['err_users_first_name']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <div>
                <label for="last_name">last_name</label>
                <input type="text" name="last_name" id="last_name">
                {% for message in get_flashed_messages(category_filter=['err_users_last_name']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <div>
                <label for="email">email</label>
                <input type="text" name="email" id="email">
                {% for message in get_flashed_messages(category_filter=['err_users_email']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <div>
                <label for="password">password</label>
                <input type="text" name="password" id="password">
                {% for message in get_flashed_messages(category_filter=['err_users_password']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <div>
                <label for="confirm_password">confirm_password</label>
                <input type="text" name="confirm_password" id="confirm_password">
                {% for message in get_flashed_messages(category_filter=['err_users_confirm_password']) %}
                <p class="err-msg">{{message}}</p>
                {% endfor %}
            </div>
            <button>Register</button>
        </form>
    </div>
```