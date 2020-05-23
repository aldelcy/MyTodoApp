from flask import Flask, request, redirect, render_template, Blueprint, jsonify
import sys, os
todo_list_routes = Blueprint( 'todo_list_routes', __name__ )

sys.path.append( os.getcwd() )
from models import db, User, TodoList, TodoListItem

@todo_list_routes.route('/todo/add/<uid>', methods=["POST"])
def add_todo( uid ):
    user = User.query.get( int( uid ) )
    title = request.form[ 'title' ]
    desc = request.form[ 'desc' ]
    color = request.form[ 'color' ]
    priority = request.form[ 'priority' ]

    newTodo = TodoList( title, desc, color, priority, user )
    db.session.add( newTodo )
    db.session.commit()

    return redirect('/user/' + str(user.id) )


@todo_list_routes.route('/todo/<id>')
def get_todo( id ):
    todo = TodoList.query.get( int( id ) )
    viewData = {
        'todo': todo,
        'user': User.query.get( todo.user.id )
    }
    return render_template('todolist.html', data = viewData)


@todo_list_routes.route('/todos/')
def get_all_todos( ):
    viewData = { 'todos': TodoList.query.all() }
    return render_template('todolist.html', data = viewData)


@todo_list_routes.route('/todo/edit/<id>')
def edit_todo( id ):
    todo = TodoList.query.get( int( id ) )
    db.session.commit()
    viewData = {}
    return redirect(f"/todo/{id}")


@todo_list_routes.route('/todo/delete/<id>')
def delete_todo( id ):
    todo = TodoList.query.get( int( id ) )
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')