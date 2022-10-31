from turtle import title
from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.sdb')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/lib', methods=['GET','POST'])
def lib():
    conn = get_db_connection()
    titles = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('lib.html',term = titles ,title='Libary')

@app.route("/login",methods = ['POST', 'GET'])
def login():
    return render_template('login.html', title='Login')

@app.route("/register",methods = ['POST', 'GET'])
def register():
    return render_template('register.html', title='Register')

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        add_title = request.form['title']
        add_author = request.form['author']

        conn = get_db_connection()
        conn.execute('INSERT INTO books (title, author) VALUES(?,?)', (add_title, add_author))
        conn.commit()
        conn.close()

    return render_template('insert.html')


@app.route('/borrowedbooks',methods=['GET','POST'])
def borrowedbooks():
    conn = get_db_connection()
    lended = conn.execute('SELECT * FROM books_borrowed').fetchall()
    conn.close()
    return render_template('borrowedbooks.html', lended=lended, title='Borrowed Books')

@app.route("/borr",methods = ['POST', 'GET'])
def borr():
    return render_template('borr.html', title='Borrower')
def borrow():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phone = request.form.get('phonenum')
    address1 = request.form['address1']
    city = request.form['city']
    if not fname:
        flash('First Name is Required!')
    elif not lname:
        flash('Last Name is Required!')
    elif not email:
        flash('Email is Required!')
    elif not phone:
        flash('Phone Number is Required!')
    elif not address1:
        flash('Address is Required!')
    elif not city:
        flash('City is Required!')
    else:
        conn = get_db_connection()
        search = conn.execute('SELECT * FROM borrowers WHERE fname LIKE ? AND lname LIKE ?',(fname, lname)).fetchall()
        rows = len(search)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)