from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/User/login')
def login():
    return 'your name is rexyang'


if __name__ == '__main__':
    app.run(debug=True)
