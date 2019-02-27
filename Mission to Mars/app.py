from flask import Flask, render_template, jsonify, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(_name_)
mongo = PyMongo(app)
@app.route("/")
def index(:)
    try:
        mars_data = mongo.db.mars_data.find_one()
        return render_templates('index.html',mars_data=mars_data)

    except:
        return redirect("http://localhost:5000/scrape", code=302)

@app.route("/scrape")
def scrape()
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars_scrape()
    mars_data.update({}, 
    mars_data_scrape,
    upsert=True)

    retrun redirect("http://localhost:5000/", code=302)

if_name_=="main":
app.run(debug=True)
    
