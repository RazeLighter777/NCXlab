from __main__ import app
from flask import Flask, render_template, request, redirect, url_for

@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    return None