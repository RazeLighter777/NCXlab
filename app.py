# flask app lmao

from routes import adduser, deluser, finduser;


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def users():
    return None

@app.route('/user/{name}', methods=['GET', 'DELETE'])
def get_user_name(name):
    return None


if(__name__ == '__main__'):
    app.run(debug=True)