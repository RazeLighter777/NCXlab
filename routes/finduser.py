from __main__ import app
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3


@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    connection = sqlite3.connect("database.db")
    users = connection.execute("SELECT * FROM users WHERE name = " + name).fetchone()
    connection.close()

    
    return jsonify({
        "phoneNumber": users[0] 
    })