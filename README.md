<h1>Data-Centric Development Milestone Project</h1>
<h2>Project Summary</h2>
<p>tech-review  The purpose is to build a full-stack site that allows users to write and give their opinion about a particular domain that allows users to create, locate, read, update and delete about all the latest tech aroud. tech-review gives access to all the reviews in the database to all users. All users can add new reviews as well as edit, locate, and delete other reviews</p>.

The project can be viewed here<a href="https://tech-review05.herokuapp.com/">here</a>

<h2>Wireframes</h2>



<h1>UX</h1>
<p>the goal in UX was to build a simple responsive website. the users can give their honest reviews about tech, view all the reviews created on the database, edit and delete them as well. The target audience for this app is anyone who has passion for tech and need to give a opnion about devices they use on daily bases and can help others to decide if the device or gadgets they are willing to buy is worth their money.
Creating a modern and user-friendly interface with easy access to all information is the key to giving users a feeling of reliability and positiveness. The app is developed in a way that anyone can creat , read ,edit or delete.
</p>

<h2>User Stories </h2>
<ul>
  <li>As a user, I want/expect:
</li>
<li>find honest and informative reviews on tech-devices</li>
<li>to view all the reviews without having to login</li>
<li>to add new recipes
</li>
<li>to edit reviews </li>
<li>to delete my reviews</li>
<li>to use a fully responsive web app
</li>
</ul>

<h2>Existing Features</h2>

<li>
Add a Recipe ([CRUD] Create or 'add' a new recipe)</li>
<li>All users can add reviews.User name will automatically populate in the add recipe form as Review Author.For selective fields,user can select the options from drop down.All the fields of the form is well explained with the 'placeholder' to make it user friendly.
Viewing Reciewss ([CRUD] Read or 'review' recipes)</li>
<li>On the reviews page, all reviews are displayed. If user wants to see a check review,the review will open in a full screen where all the details of the review can be found.
Update a Recipe ([CRUD] Update recipes)</li>
<li>Users can update or 'edit' review on Edit page.</li>
<li>Delete a Recipe ([CRUD] Delete recipes)</li>
<li>Users can delete or 'remove' reviews. </li>
  
  <h2>Features Left to Implement</h2>
<li>Register User allowing anybody can register for free.
</li>
<li>Add full Specifications for the product 
</li>
<li>Add full prise range of the product 
</li>
<li>Log in and log out features
</li>
<li>Delete option that will only be visible for a user on their own review pages.</li>
<li>Edit option that will only be visible for a user on their own review pages.
</li>
<li>add more js/j query features to make it more user friendly</li>
<li>Social share buttons</li>
<li>Comments section</li>

<h1>Technologies Used</h1>
<h3><a href="https://github.com/">GitHub</a></h3>
<li>Used as remote storage of my code online.
</li>
<h3><a href="https://pip.pypa.io/en/stable/installing/">PIP</a></h3>
<li>for installation of necessary tools.
</li>
<h1>Front-End Technologies</h1>
<h3><a href="https://jquery.com/">JQuery</a></h3>
<li>The project uses JQuery to simplify DOM manipulation.</li>
<h3><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">Javascript</a></h3>
<li>I used JavaScript from the Google Maps API website and for the reset button</li>
<h3><a href="https://en.wikipedia.org/wiki/HTML5">HTML5</h3></a>
<li>HTML5 was used for the semantic structure and presenting the content of the webpage.</li>
<h3><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3">CSS3</h3></a>
<li>CSS3 was used for the styling of the content to produce an aesthetically pleasing viewing experience.</li>
<h3><a href="https://materializecss.com/">Materialize</h3></a>
<li>Used as the design framework.</li>

<h1>Back-End Technologies
</h1>
<h3><a href="https://www.python.org/">Python</h3></a>
<li>back-end programming language used in this project.</li>
<h3><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</h3></a>
<li>microframework for building and rendering pages.</li>
<h3><a href="https://www.mongodb.com/">MongoDB Atlas</h3></a>
<li>NoSQL database for storing back-end data.</li>
<h3><a href="https://api.mongodb.com/python/current/">PyMongo</h3></a>
<li>for Python to get access the MongoDB database.</li>
<h3><a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</h3></a>
<li>templating language for Python, to display back-end data in HTML.</li>
<h3><a href="https://heroku.com/">Heroku</h3></a>
<li>to host the project.</li>

<h1>Libraries
</h1>
<h3><a href="https://fontawesome.com/">Font Awesome</h3></a>
<li>Font Awesome was used for the social links, mainly the social media icons for a professional finish.</li>
<h3><a href="https://fonts.google.com/">Google Fonts</h3></a>
<li>I used Google Fonts for the font families.</li>





<h1>Depolyment</h1>
<h3>Deployment to Heroku
</h3>
In order to deploy my project to Heroku I have completed the following steps, you can view it <a href="http://tech-review05.herokuapp.com/get_reviews">here</a>.
<li>Created a Procfile with the command echo web: python run.py > Procfile.</li>
<li>Created a requirement.txt file so Heroku know what python modules it will need to run my application with the command pip freeze > requirements.txt
</li>
<li>Created a new branch to test deployment to heroku changing MONGO_URI from local to mongo atlas, changed app.run() to set debug to False.
</li>
<li>Created a new project on heroku and in the deploy section linked my github repository with heroku in order to deploy straight from the source.
 </li>
<li>Configured any environment variables in Heroku App Settings > Config Vars such as my Secret Key, IP PORT and MONGO_URI.
</li>
<li>Finalised all code, and made sure that it was production ready and ensured that my .gitignore was not uploading any secret keys.</li>
<li>Deployed the application from heroku admin page using linked repository and master branch.
</li>
<li>The application is now fully deployed to Heroku
</li>
