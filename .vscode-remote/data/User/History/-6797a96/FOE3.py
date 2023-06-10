from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
import os
load_dotenv()

db = SQLAchemy()
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


    @app.route