"""
In this file we are going to create sqlalchemy models
for mysql database
"""
# importing db from api 
from api import db
from  datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.String(20), nullable=False, default = datetime.strftime(datetime.now(), "%s"))
    description = db.Column(db.String(1000), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="Incomplete")
    created_date=db.Column(db.DateTime, default=datetime.now())