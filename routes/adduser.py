from __main__ import app
from flask import Flask, render_template, request, redirect, url_for

@app.route('/users', methods=['POST'])
def users():
    return None