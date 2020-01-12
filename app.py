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
COLLECTION_NAME3 = 'country'
COLLECTION_NAME4 = 'price'

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

@app.route('/about')
def about():
    n = conn[DATABASE_NAME][COLLECTION_NAME].find().count()
    from datetime import date
    today = date.today()
    date = today.strftime("%d %B %Y")
    return render_template("about.html", n=n, date=date)

# Add Picture Section
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


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
    
    if "wine_image" in request.files:
        wine_image = request.files['wine_image']
        mongo.save_file(wine_image.filename, wine_image)
    
    conn[DATABASE_NAME][COLLECTION_NAME].insert({
        "firstname" : firstname.capitalize(),
        "lastname" : lastname.capitalize(),
        "price" : price,
        "country" : country,
        "winetype" : winetype,
        "label" : label,
        "winery" : winery.capitalize(),
        "description" : description,
        "wine_image" : wine_image.filename
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
    country = request.args.get('country')
    criteria= {} 
    
    if type and type != 'Type':
        criteria['winetype'] = type
    else:
        type = 'Wine Type'
        
    if cost and cost != 'Cost':
        criteria['price'] = cost
    else:
        cost ='Wine Price'
        
    if country and country != 'Country':
        criteria['country'] = country
    else:
        country = 'Country'
    
    # products = conn[DATABASE_NAME][COLLECTION_NAME].find(criteria)
    # print(criteria)
    wine = conn[DATABASE_NAME][COLLECTION_NAME].find(criteria)
    winetype = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    countries = conn[DATABASE_NAME][COLLECTION_NAME3].find()
    price = conn[DATABASE_NAME][COLLECTION_NAME4].find()
    
    
    return render_template("search.html", title="search", wine=wine,type=type,cost=cost,country=country,winetype=winetype,countries=countries,price=price)

# Add Wine Detail Section
@app.route('/wine_detail/<wine_id>')
def wine_detail(wine_id):
    wines = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        "_id": ObjectId(wine_id)
    })
    
    return render_template("wine_detail.html",wines=wines)
    
    
# Edit Wine Information Section
@app.route('/edit_wine/<wines_id>')
def edit_wine(wines_id):
    winetype = conn[DATABASE_NAME][COLLECTION_NAME2].find()
    country = conn[DATABASE_NAME][COLLECTION_NAME3].find()
    price = conn[DATABASE_NAME][COLLECTION_NAME4].find()
    wine = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        "_id": ObjectId(wines_id)
    })
    
    return render_template("edit_wine.html",winetype=winetype,country=country,price=price,wine=wine)
    
    
# Submit Edit Wine Detail Section
@app.route('/edit_wine/<wines_id>', methods=['POST'])
def submit_edit_wine(wines_id):
    wine = conn[DATABASE_NAME][COLLECTION_NAME].find_one({
        "_id": ObjectId(wines_id)
    })
    
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    price = request.form.get('price')
    country = request.form.get('country')
    winetype = request.form.get('winetype')
    label = request.form.get('label')
    winery = request.form.get('winery')
    description = request.form.get('description')
    
    if "wine_image" in request.files and request.files['wine_image'].filename != "":
        wine_image = request.files['wine_image']
        image_filename = wine_image.filename
        mongo.save_file(wine_image.filename, wine_image)
    else:
        image_filename = wine['wine_image']   
    
    # Update MONGODB wine information
    conn[DATABASE_NAME][COLLECTION_NAME].update({
         "_id": ObjectId(wines_id)
    }, {
        "firstname" : firstname.capitalize(),
        "lastname" : lastname.capitalize(),
        "price" : price,
        "country" : country,
        "winetype" : winetype,
        "label" : label,
        "winery" : winery.capitalize(),
        "description" : description,
        "wine_image" :image_filename
    })
    
    return redirect(url_for('search'))

    
# Delete Wine Information Section
@app.route('/delete_product/<wines_id>') 
def delete_wine(wines_id):
    wines = conn[DATABASE_NAME][COLLECTION_NAME].remove({
        '_id': ObjectId(wines_id)
    })
    
    return redirect(url_for('search'))
    


    

    



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)