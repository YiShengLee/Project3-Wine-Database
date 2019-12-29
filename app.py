import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import re


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Project_3'
# app.config["COLLECTION_NAME"] = 'wine'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
conn = pymongo.MongoClient(os.getenv("MONGO_URI"))
DATABASE_NAME = 'Project_3'
COLLECTION_NAME = 'wine'
COLLECTION_NAME2 = 'review'

# Initilize Pymongo
mongo = PyMongo(app)

# Main Route
@app.route('/')
@app.route('/index')
# def index():
#     wine = conn[app.config["MONGO_DBNAME"]][app.config["COLLECTION_NAME"]].find()
#     return render_template('index.html', wine = wine)

# def index():
#     return render_template("index.html", 
#                           index=mongo.db.wine.find())

def index():
    return render_template("index.html", title="index")

# Add Wine Section
@app.route('/add_wine')
def add_wine():
    return render_template("add.html", title="add_wine")

@app.route('/add_wine', methods=['POST']) #To add the new wine information to mongodb database
def insert_wine():
    price = request.form.get('price')
    country = request.form.get('country')
    province = request.form.get('province')
    description = request.form.get('description')
    winetype = request.form.get('winetype')
    label = request.form.get('label')
    
    
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    # points = request.form.get('points')
    label = request.form.get('label')
    
    conn[DATABASE_NAME][COLLECTION_NAME].insert({
        "price" : price,
        "country" : country,
        "province" : province,
        "description" : description,
        "winetype" : winetype,
        "label" : label
    })
    
    conn[DATABASE_NAME][COLLECTION_NAME2].insert({
        "firstname" : firstname,
        "lastname" : lastname,
        # "points" : points,
        "label" : label
    })
    

    
    # print(name,points,variety,title)
    # flash("You have added a new wine.")
    return redirect("/")
    
# Add Search Section
@app.route('/search')
def search():
    wine = conn[DATABASE_NAME][COLLECTION_NAME].find()
    return render_template("search.html", title="search", wine=wine)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)