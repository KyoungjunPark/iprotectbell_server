# -*- encoding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect, url_for, session

index_blueprint = Blueprint('index', __name__)
