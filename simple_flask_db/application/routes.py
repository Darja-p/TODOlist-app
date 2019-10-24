from flask import current_app as app
from flask import render_template

from .hello import HelloApi
# from .books import BookApi
from .todos import TodosApi
from .models import TODOS

tasks = TODOS.query.order_by((TODOS.due_date).asc()).all()


app.register_blueprint(HelloApi, url_prefix='/hello')
app.register_blueprint(TodosApi, url_prefix='/todos')

# homepage
@app.route('/')
def hello():
    return render_template('hello.html',tasks=tasks)

