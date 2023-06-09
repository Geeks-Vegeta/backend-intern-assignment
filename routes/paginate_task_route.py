from flask_restful import Resource
import controllers.paginate_controller as task


# login class
class PaginateTaskRoute(Resource):
    
    def get(self):
        return task.getTasks()