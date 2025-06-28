from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/login')
def log():
    return render_template('login.html')