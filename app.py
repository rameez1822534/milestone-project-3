import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "tech-data"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html",
    reviews=mongo.db.reviews.find())


'''Show Add review'''


@app.route('/add_reviews')
def add_reviews():
    return render_template('add_reviews.html',
    categories=mongo.db.categories.find())


'''Update Review'''


@app.route('/insert_reviews', methods=['POST'])
def insert_reviews():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))    


'''shows the review page of its own by clicking view.'''


@app.route('/review_display/<review_id>')
def review_display(review_id):
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})    
    return render_template('review_display.html', reviews=the_review)


''' Edit Review '''


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_review.html',
    reviews=review,categories=all_categories)


'''Update Review'''


@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    review = mongo.db.reviews
    review.update({'_id': ObjectId(review_id)},
        {
            'device_make': request.form.get('device_make'),
            'device_model': request.form.get('device_model'),
            'device_review': request.form.get('device_review'),
            'device_type': request.form.get('device_type'),
            'device_ratings': request.form.get('device_ratings'),
            'deviceimage_url': request.form.get('deviceimage_url'),
        })
    return redirect(url_for('get_reviews'))    


'''Delete Reviews'''

 
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))


'''Login'''


@app.route('/login')
def login():
    return render_template('login.html')    


'''Show Categories'''


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


'''Delete Categories'''


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


'''Edit Categories'''


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


'''Update Categories'''


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_type': request.form.get('category_type')})
    return redirect(url_for('get_categories'))


'''Add Categories'''


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_type': request.form.get('category_type')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


'''Show Add Categories page '''


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")), 
            debug=True)
