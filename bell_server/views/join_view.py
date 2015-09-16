# -*- encoding: utf-8 -*-

from flask import Blueprint, request, render_template, redirect, url_for, session, g

join_blueprint = Blueprint('join', __name__)

@join_blueprint.route('/join', methods=['POST'])
def join():
    error_code = 200
    error_message = "Default"

    if request.method == 'POST':
        if valid_serialNum(request.form['serialNum']):
            if valid_id(request.form['user_id']):
                cur = g.db.execute('insert into user(user_id, user_password, bell_id) values(?,?,?)'
                        ,[request.form['user_id'],request.form['user_password'], request.form['serialNum']])
                g.db.commit()
            else:
                error_code = 404
                error_message = "Already id is exist"
        else:
            error_code = 404
            error_message = "This serial number is incorrect or already used by other user"
    else:
        error_code = 404
        error_message = "You must send POST communication"

    if error_code == 200:
        return "ok"
    else:
        return error_message, error_code

def valid_serialNum(serialNum):
    cur = g.db.execute('select count(*) from bell where id = ?',[serialNum])
    g.db.commit()
    result = cur.fetchone()

    if result[0] == 0:
        return False
    else:
        cur = g.db.execute('select count(*) from user where bell_id = ?', [serialNum])
        g.db.commit()
        result = cur.fetchone()

        if result[0] == 0:
            return True
        else:
            return False

def valid_id(user_id):
    cur = g.db.execute('select count(*) from user where user_id = ?',[user_id])
    g.db.commit()
    result = cur.fetchone()

    if result[0] == 0:
        return True
    else:
        return False


