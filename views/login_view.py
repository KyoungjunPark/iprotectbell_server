from flask import Blueprint, request, render_template, redirect, url_for, session, g
import os
import binascii

login_blueprint  = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['user_id'], request.form['user_password']):
            token = make_token()
            cur = g.db.execute('select count(*) from token where user_id = ?'
                    ,[request.form['user_id']])
            g.db.commit()
            result = cur.fetchone()
            if result[0] == 0:
                cur = g.db.execute('insert into token(user_id, user_token) values(?,?)'
                ,[request.form['user_id'], token])
            else:
                cur = g.db.execute('update token set user_token=? where user_id=?'
                        ,[token, request.form['user_id']])
            g.db.commit()
            return token, 200
        else:
            return "This id or password is not correct!",404

def make_token():
   return binascii.hexlify(os.urandom(12))

def valid_login(user_id, user_password):
    cur = g.db.execute('select count(*) from user where user_id= ? AND  user_password= ?'
            ,[user_id, user_password])
    g.db.commit()
    result = cur.fetchone()

    if result[0]  == 0:
        return False
    else:
        return True

