import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "tech-data"
app.config["MONGO_URI"] = "mongodb+srv://rameez1:XCoDWa4q3nYSVrwp@myfirstcluster-cbmmr.mongodb.net/tech-data?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)