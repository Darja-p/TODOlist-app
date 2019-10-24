from flask import Blueprint, jsonify, request

from . import db
from .models import TODOS

TodosApi = Blueprint('todos_api', __name__)


@TodosApi.route('/create', methods=['POST'])
def create_task():

    try:
        task = TODOS.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(task)
    db.session.commit()
    return jsonify(), 200


@TodosApi.route('/<due_date>', methods = ['GET'])
def get_tasks(due_date):
    tasks = TODOS.query.filter(TODOS.due_date == due_date).all()
    return jsonify([x.to_dict() for x in tasks]), 200

@TodosApi.route('/all', methods = ['GET'])
def get_all():
    tasks = TODOS.query.all ()  #order_by(TODOS.due_date).
    return jsonify ([x.to_dict () for x in tasks]) , 200

@TodosApi.route('/<id>', methods = ['DELETE'])
def delete(id):
    task = TODOS.query.filter(TODOS.id == id).first()  #order_by(TODOS.due_date).
    db.session.delete (task)
    db.session.commit ()
    return jsonify () , 200


@TodosApi.route('/<id>', methods=['PUT'])
def update_task(id):

    try:
        task = TODOS.query.filter_by(id =id).first()
        task.description = request.json.get ('description' , task.description)
        task.due_date= request.json.get ('due_date' , task.due_date)
        db.session.commit ()
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.commit()
    return jsonify(), 200

