from flask import Blueprint, render_template
from .models import TODOS

HelloApi = Blueprint('hello_api', __name__)
tasks = TODOS.query.order_by((TODOS.due_date).asc()).all()

@HelloApi.route('/<name>')
def hello_user(name):
    return render_template('hello.html', user=name, tasks=tasks)