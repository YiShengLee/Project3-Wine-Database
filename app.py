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
COLLECTION_NAME2 = 'winetype'

app.secret_key = "secret"

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
    winetype = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    return render_template("add.html", title="add_wine",winetype=winetype)

@app.route('/post_wine', methods=['POST']) #To add the new wine information to mongodb database
def post_wine():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    price = request.form.get('price')
    country = request.form.get('country')
    winetype = request.form.get('winetype')
    label = request.form.get('label')
    winery = request.form.get('winery')
    description = request.form.get('description')
    
    conn[DATABASE_NAME][COLLECTION_NAME].insert({
        "firstname" : firstname.capitalize(),
        "lastname" : lastname.capitalize(),
        "price" : price,
        "country" : country,
        "winetype" : winetype,
        "label" : label,
        "winery" : winery.capitalize(),
        "description" : description
    })
    
    
    # print(name,points,variety,title)
    flash('The wine has successfully been updated!', 'success')
    return redirect("/add_wine")
    
# Add Search Section
@app.route('/search')
def search():
    # print(request.args)
    type = request.args.get('type')
    cost = request.args.get('cost')
    brand = request.args.get('brand')
    criteria= {} 
    
    if type and type != 'Type':
        criteria['winetype'] = type
    else:
        type = 'Type'
        
    # if cost and cost != 'Cost':
    #     criteria['cost'] = cost
    # else:
    #     cost ='Cost'
        
    # if brand and brand != 'Brand':
    #     criteria['brand'] = brand
    # else:
    #     brand = 'Brand'
    
    # products = conn[DATABASE_NAME][COLLECTION_NAME].find(criteria)
    print(criteria)
    winetype = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    wine = conn[DATABASE_NAME][COLLECTION_NAME].find(criteria)
    # print(list(wine))
    return render_template("search.html", title="search", wine=wine,type=type,cost=cost,brand=brand,winetype=winetype)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)