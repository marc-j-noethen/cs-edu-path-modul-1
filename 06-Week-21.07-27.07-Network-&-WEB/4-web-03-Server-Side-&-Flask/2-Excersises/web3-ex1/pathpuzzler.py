from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the Route Master Home Page!'

@app.route('/status')
def status():
    return 'Application is running.'

@app.route('/info')
def info():
    now = datetime.now()
    return  f"Current date and time: {now}"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route("/calculate/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 + num2}"

@app.route("/calculate/subtract/<int:num1>/<int:num2>")
def subtract(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 - num2}"

@app.route("/calculate/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 * num2}"

@app.route("/calculate/divide/<int:num1>/<int:num2>")
def divide(num1, num2):
    return f"The sum of {num1} and {num2} is {num1 / num2}"

if __name__ == '__main__':
    app.run(debug=True)