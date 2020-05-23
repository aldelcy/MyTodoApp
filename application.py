from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
import sys, os
from models import db, User, TodoList, TodoListItem

app = Flask(__name__)
app.config['DEBUG'] == True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDatabase.db'
app.config['SQLALCHEMY_ECHO'] = True

db.app = app
db.init_app(app)

sys.path.append( os.getcwd() + "/controllers/" )

from user_controller import user_routes
app.register_blueprint( user_routes )

from todo_list_controller import todo_list_routes
app.register_blueprint( todo_list_routes )

from todo_list_item_controller import todo_list_item_routes
app.register_blueprint( todo_list_item_routes )

@app.route('/')
def get_all_users():
    viewData = { 'users': User.query.all() }
    return render_template('index.html', data = viewData)

if __name__ == "__main__":
    app.run()