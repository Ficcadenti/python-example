from flask import Flask, escape, request

app = Flask(__name__)

'''
    https://flask.palletsprojects.com/en/1.1.x/quickstart/
    env FLASK_APP=hello.py flask run
'''

@app.route('/', methods = ['GET'])
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'