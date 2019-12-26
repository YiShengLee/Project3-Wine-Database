import os
from flask import Flask, render_template, redirect, request, url_for
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
COLLECTION_NAME2 = 'country'
COLLECTION_NAME3 = 'review'

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

@app.route('/add_wine')
def add_wine():
    return render_template("add.html", title="add_wine")
    
@app.route('/search')
def search():
    wine = conn[DATABASE_NAME][COLLECTION_NAME].find()
    return render_template("search.html", title="search", wine=wine)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)