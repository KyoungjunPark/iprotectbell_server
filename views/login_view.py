from flask import Blueprint, request, render_template, redirect, url_for, session, g

login_blueprint  = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['user_id'], request.form['user_password']):
            return "ok"
        else:
            return "You are idiot",404


def valid_login(user_id, user_password):
    cur = g.db.execute('select count(*) from user where user_id= ? AND  user_password= ?'
            ,[user_id, user_password])
    g.db.commit()
    result = cur.fetchone()

    if result[0]  == 0:
        return False
    else:
        return True

