import json

from flask import Blueprint, request, render_template, redirect, url_for, session, g

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/', methods=['GET'])
def home():
    return "do nothing"
