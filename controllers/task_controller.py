from flask_restful import abort, marshal_with, fields, reqparse
from flask import request
from api import db
from db.model import Task

parse = reqparse.RequestParser()
parse.add_argument("title", type=str, help="title is required")
parse.add_argument("description", type=str, help="body is required")
parse.add_argument("due_date", type=str, help="due_date is required")
parse.add_argument("status", type=str, help="status is required")

#  json serialization
resource_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "status":fields.String,
    "due_date":fields.String,
    "created_date": fields.String
}


@marshal_with(resource_fields)
def createTask():
    args = parse.parse_args()

    is_title_exist = Task.query.filter_by(title=args['title']).first()

    if args['due_date']:
        if len(args['due_date'])!=10:
            abort(400, message="Make sure your due_date is timestamp of length 10, follow this website https://www.epochconverter.com/")

    if not is_title_exist:
        post = Task(title=args['title'], description=args['description'], due_date=args['due_date'])
        db.session.add(post)
        db.session.commit()
        return post,201
    abort(400, message="Task already exists")
   

@marshal_with(resource_fields)
def getTaskById():
    id = request.args.get('id')
    if not id:
        alltask = Task.query.all()
        return alltask,200
    else:
        task = Task.query.filter_by(id=id).first()
        if task is None:
            abort(400, message="No task")

        else:
            return task



def deleteTask():

    id = request.args.get('id')

    # checking if post is present
    task = Task.query.filter_by(id=id).first()
    
    # if not post
    if not task:
        abort(404, message="task is not present can't delete")

    
    # deleting from db
    db.session.delete(task)
    db.session.commit()

    return {"message":"deleted successfully"},200


@marshal_with(resource_fields)
def updateTask():

    id = request.args.get('id')

    args = parse.parse_args()
    # checking if task is present
    task = Task.query.filter_by(id=id).first()
    
    # if not task
    if not task:
        abort(404, message="task is not present can't update")

    if args['status'] not in ["Incomplete", "InProgress","Completed"]:
        abort(400, message="status should be either 'Incomplete', 'InProgress' or 'Completed'")
    
    if args['due_date']:
        if len(args['due_date'])!=10:
            abort(400, message="Make sure your due_date is timestamp of length 10, follow this website https://www.epochconverter.com/")


    task.title = args['title']
    task.description = args['description']
    task.status= args['status']
    task.due_date=args['due_date']
    
    # commiting actions
    db.session.commit()

    return task,200