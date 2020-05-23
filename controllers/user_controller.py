from flask import Flask, request, redirect, render_template, Blueprint, jsonify
import sys, os
user_routes = Blueprint( 'user_routes', __name__ )

sys.path.append( os.getcwd() )
from models import db, User

@user_routes.route('/user/add')
def add_user( ):
    viewData = {}
    return redirect('/')


@user_routes.route('/user/<id>')
def get_user( id ):
    viewData = { 'user': User.query.get( int( id ) ) }
    return render_template('user.html', data = viewData)


@user_routes.route('/users/')
def get_all_users( ):
    viewData = { 'users': User.query.all() }
    return render_template('user.html', data = viewData)


@user_routes.route('/user/edit/<id>')
def edit_user( id ):
    user = User.query.get( int( id ) )
    db.session.commit()
    viewData = {}
    return redirect(f"/user/{id}")


@user_routes.route('/user/delete/<id>')
def delete_user( id ):
    user = User.query.get( int( id ) )
    db.session.delete(user)
    db.session.commit()
    return redirect('/')