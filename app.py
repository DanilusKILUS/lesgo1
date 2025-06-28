from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('surikat.db', check_same_thread=False)
curs = conn.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
)
''')
conn.commit()


def add_user(name, email, passw):
    curs.execute('''
    INSERT INTO users(
        name,
        email,
        password             
    )
    VALUES (?, ?, ?),
    (name, email, passw)
    ''')
    conn.commit()

def search_email(email):
    curs.execute('SELECT * FROM users WHERE email = ?', (email, ))
    return curs.fetchone()


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def reg():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        passw = request.form.get('Password')
    return render_template('register.html')

@app.route('/login')
def log():
    return render_template('login.html')