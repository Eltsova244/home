from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
load_dotenv()

db = SQLAlchemy()
app = Flask(_name_)
app config["SQlALCHEMY_DATA_BASE_URI"] = os.getenv("HOGWARTS_URL")
db.init_app(app)

class Student(db.Model):
    id = db.Column(db.Integer, primery_key=True)
    fname = db.Column(db.String)
    lname= db.Column(db.String)
    house= db.Column(db.String)

    def_init_(self, fname, lname, house):
        self.fname = fname
        self.lname = lname
        self.house = house


    @app.route('/submit')
    def submit():
 fname = request.form.get('fname')
    lname = request.form.get('lname')
    house = request.form.get('house')
    student = Student(fname, lname, house)
    db.session.add(student)
    db.session.commit()
    return render_template('success.html')
