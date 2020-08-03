import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "tech-data"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())


@app.route('/add_review')
def add_review():
    return render_template('addreviews.html')


if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0")
            port=(os.environ.get("PORT", 5000)), debug=False)