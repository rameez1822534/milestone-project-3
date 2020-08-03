import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "tech-data"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())


@app.route('/add_reviews')
def add_reviews():
    return render_template('add_reviews.html',categories=mongo.db.categories.find())

@app.route('/insert_reviews', methods=['POST'])
def insert_reviews():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))    

@app.route('/review_display/<review_id>')
def review_display(review_id):
    review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})    
    return render_template('review_display.html', reviews=review)

@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    review = mongo.db.reviews1.find_one({"_id": ObjectId(review_id)})
    all_categories = mongo.db.categories.find()
    print(edit_review)
    return render_template('edit_review.html', reviews1=review, categories=all_categories)

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")), 
            debug=True)