from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User( db.Model ):
    id          = db.Column( db.Integer, primary_key = True )
    username    = db.Column( db.String(10) )
    password    = db.Column( db.String(6) )
    full_name   = db.Column( db.String(10) )
    email       = db.Column( db.String(20) )
    todos       = db.relationship( 'TodoList', backref = "user" )

    def __init__( self, username, password, full_name, email ):
        self.username   = username
        self.password   = password
        self.full_name  = full_name
        self.email      = email

class TodoList( db.Model ):
    id          = db.Column( db.Integer, primary_key = True )
    title       = db.Column( db.String(10) )
    desc        = db.Column( db.String(200) )
    color       = db.Column( db.String(10) )
    priority    = db.Column( db.Integer )
    user_id     = db.Column( db.Integer, db.ForeignKey('user.id')  )
    todoitems   = db.relationship( 'TodoListItem', backref = "todo" )

    def __init__( self, title, desc, color, priority, user ):
        self.title      = title
        self.desc       = desc
        self.color      = color
        self.priority   = priority
        self.user       = user

class TodoListItem( db.Model ):
    id          = db.Column( db.Integer, primary_key = True )
    title       = db.Column( db.String(10) )
    desc        = db.Column( db.String(200) )
    color       = db.Column( db.String(10) )
    priority    = db.Column( db.Integer )
    done        = db.Column( db.Integer )
    todo_id     = db.Column( db.Integer, db.ForeignKey('todo_list.id')  )

    def __init__( self, title, desc, color, priority, todo ):
        self.title      = title
        self.desc       = desc
        self.color      = color
        self.priority   = priority
        self.done       = 0
        self.todo       = todo