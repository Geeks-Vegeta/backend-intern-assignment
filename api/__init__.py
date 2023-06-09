from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "sdfhs8dhfuijekfodjiujjj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'


api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from routes.home_route import HomeRoute
from routes.paginate_task_route import PaginateTaskRoute
from routes.task_route import TaskRoute

api.add_resource(HomeRoute,"/")
api.add_resource(TaskRoute,"/task", "/task/<id>")
api.add_resource(PaginateTaskRoute,"/tasks","/tasks/<page>/<per_page>")
