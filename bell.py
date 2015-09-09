import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash, jsonify
import json
from contextlib import closing

import views

app = Flask(__name__)
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'bell.db'),
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))

app.config.from_object(__name__)
views.register_views(app)

def connect_db():
    rv =sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['user_id'], request.form['user_name']):
            return log_the_user_in(request.form['user_name'])
        else:
            error = 'Invalid username/id'
    return "tmp"


#GET communication test
@app.route('/add_GET', methods=['GET'])
def add_GET():
    g.db.execute('insert into user (user_id, user_name) values (?, ?)',
            [request.args.get('user_id',''), request.args.get('user_name','')])
    g.db.commit()
    return home()

#POST communication test
@app.route('/add_POST', methods=['GET','POST'])
def add_POST():
    if request.method == 'POST':
        g.db.execute('insert into user (user_id, user_name) values (?, ?)',
                [request.form['user_id'], request.form['user_name']])
        g.db.commit()
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


