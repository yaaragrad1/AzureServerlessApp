from flask import Flask
from math import factorial
# app is an instance of class Flask
app = Flask(__name__)

# route is just a URL that returns a template page
@app.route('/hello/<name>')
def hello(name):
    print("Adding a print to log")
    return 'Hello %s, serverless computing is here to stay!' % name

@app.route('/factorial/<int:id>')
def fact(id):
    n = factorial(id)
    return f'factorial for {id} is {n}'