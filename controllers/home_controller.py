
from flask import jsonify, make_response

def home():
    return make_response(jsonify({"messgae":"Inital Route"}), 200)