from flask import Flask, request, redirect, render_template, Blueprint, jsonify
import sys, os
todo_list_item_routes = Blueprint( 'todo_list_item_routes', __name__ )

sys.path.append( os.getcwd() )
from models import db, User, TodoList, TodoListItem


@todo_list_item_routes.route('/todo_item/add/<todoid>', methods=["POST"])
def add_todo_item( todoid ):
    todo = TodoList.query.get( int( todoid ) )
    user = todo.user
    title = request.form[ 'title' ]
    desc = request.form[ 'desc' ]
    color = request.form[ 'color' ]
    priority = request.form[ 'priority' ]

    newTodoItem = TodoListItem( title, desc, color, priority, todo )
    db.session.add( newTodoItem )
    db.session.commit()

    return redirect('/todo/' + str(todo.id) )


@todo_list_item_routes.route('/todo_item/<id>')
def get_todo_item( id ):
    todo_item = TodoListItem.query.get( int( id ) )
    viewData = {
        'todo_item': todo_item,
        'todo': todo_item.todo
    }
    return render_template('todolist.html', data = viewData)


@todo_list_item_routes.route('/todo_items/')
def get_all_todo_items( ):
    viewData = { 'todo_items': TodoList.query.all() }
    return render_template('todolist.html', data = viewData)


@todo_list_item_routes.route('/todo_item/edit/<id>')
def edit_todo_item( id ):
    todo_item = TodoListItem.query.get( int( id ) )
    todo = todo_item.todo

    todo_item.done = int( request.args.get( 'done' ) )

    db.session.commit()
    viewData = {}
    return redirect(f"/todo/{todo.id}")


@todo_list_item_routes.route('/todo_item/delete/<id>')
def delete_todo_item( id ):
    todo_item = TodoListItem.query.get( int( id ) )
    todo = todo_item.todo

    db.session.delete(todo_item)
    db.session.commit()

    return redirect(f"/todo/{todo.id}")