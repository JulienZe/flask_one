from flask import Flask
from flask import make_response
from flask import request
from flask import redirect
from flask import abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    # user_agent = request.headers.get('User_agent')
    # return '<p>Your browser is %s</p>' % user_agent
    # return '<h1>Bad Request<h1>',400
    # response = make_response('<h1> This document carries a cookie!</h1>')
    # response.set_cookie('answer','42')
    # return response
    return redirect('http://www.example.com')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!<h1>' % name


# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return

if __name__ == '__main__':
    app.run(debug=True)
