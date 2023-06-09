from flask_restful import Resource
import controllers.task_controller as task


# login class
class TaskRoute(Resource):

    def post(self):
        return task.createTask()
    
    def get(self):
        return task.getTaskById()
    
    def delete(self):
        return task.deleteTask()
    
    def put(self):
        return task.updateTask()