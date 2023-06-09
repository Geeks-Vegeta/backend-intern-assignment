from flask import request,jsonify
from flask_restful import abort
from api import db
from db.model import Task


def getTasks():
    if request.args.get('page') is None and request.args.get('per_page') is None:
        abort(400, message="make sure to pass per_page and page query parameter")
    else:
        page= int(request.args.get('page'))
        per_page= int(request.args.get('per_page'))

        
        alltask = Task.query.order_by(Task.id.asc())
        alltask = alltask.paginate(page=page, per_page=per_page)
        return jsonify({
            'page': page,
            'per_page': per_page,
            'has_next': alltask.has_next,
            'has_prev': alltask.has_prev,
            'page_list': [iter_page if iter_page else '...' for iter_page in alltask.iter_pages()],
            'posts': [{
                'id': p.id,
            } for p in alltask.items]
        })
            