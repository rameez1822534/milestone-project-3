<h1>Tech-Review</h1>
<h2>Project Summary</h2>
<p>The purpose is to build a full-stack site that allows users to write and give their opinion about a particular domain and at the same time allow users to create, locate, read, update and delete the reviews about all the latest tech aroud. tech-review gives access to all the reviews in the database to the users. All users can add new reviews as well as edit, locate, and delete other reviews</p>

The project can be viewed <a href="https://tech-review05.herokuapp.com/">here</a>

<h2>Wireframes</h2>
<p>Wireframes.cc tool has been used to creat the wireframes
Initial Wireframes for the site: <a href="https://github.com/rameez1822534/milestone-project-3/tree/master/wireframes">Wireframes</a>| 


<h1>UX</h1>
<p>the goal in UX was to build a simple responsive website. the users can give their honest reviews about tech, view all the reviews created on the database, edit and delete them as well. The target audience for this app is anyone who has passion for tech and need to give a opinion about devices they use on daily bases and can help others to decide if the device or gadgets they are willing to buy is worth their money.
The purpose was to creat a modern and user-friendly interface with easy access to all information to give users a feeling of reliability and positiveness. The app is developed in a way that anyone can creat , read ,edit or delete.
</p>

<h2>User Stories </h2>
<ul>
  <li>As a user, I want/expect:
</li>
<li>find honest and informative reviews on tech-devices</li>
<li>to view all the reviews without having to login</li>
<li>to add new reviews
</li>
<li>to edit reviews </li>
<li>to delete my reviews</li>
<li>to use a fully responsive web app
</li>
</ul>

<h2>Existing Features</h2>

<li>
Add a Review ([CRUD] Create or 'add' a new review)</li>
<li>All users can add reviews , user can automatically populate the reviews database and all new reviews added by the user will be visible on the home page.All the fields of the form is well explained with the 'placeholder' to make it user friendly.
Viewing Reviews ([CRUD] Read or write )</li>
<li>On the reviews page, all reviews are displayed. If user wants to see a check review,the review will open in a full screen where all the details of the review can be found.
Update a Review([CRUD] Update reviews)</li>
<li>Users can update or 'edit' review on Edit page.</li>
<li>Delete a Recipe ([CRUD] Delete recipes)</li>
<li>Users can delete or 'remove' reviews. </li>
  
  <h2>Features Left to Implement</h2>
<li>Register User allowing anybody can register for free.
</li>
<li>only Registered User can add edit update or delete.
</li>
<li>Add full Specifications for the product 
</li>
<li>Add full price range of the product 
</li>
<li>Log in and log out features
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
<li>Deployed the application from heroku admin page using linked repository and master branch.
</li>
<h1>Testing</h1>

Testing was performed in 3 different ways.
- Browser Testing
- User testing
- Manual Testing

<h3>Browser Testing</h3>
The app has been tested on various browsers which includes chrome , internet explorer and firefox and there has not been any issues.

<h3>User testing
</h3>
….

<li>...</li>

<h3>Manual Testing
</h3>
View | Add | Edit | Delete | Search
<h4>All reviews and single reviews display
</h4>
<li>...</li>
<h4>Add New Reviews
</h4>

<h4>Edit Review
</h4>
<li>Edit review button is visible on the review page. Once clicked it opens a page with a form that allows the user to edit the review. </li>
<h4>Delete review
</h4>
<li>Delete button is visible  on the review page.  Once clicked it deletes the review from the database</li>

<h2>Issues discovered while testing and how they were rectified.</h2>
<li>This site was tested across multiple mobile devices (iPhone 4, 5, 7, 8, X, iPad, iPad Pro, Galaxy S5, Pixel 2, and Pixel 2XL) to ensure compatibility and responsiveness.  </li>
<li>For testing the responsive aspect of the website I used a Google Chrome Developer Tools</li>
<li>Side nav - the mobile side nav was not functioning correctly. This was rectifies by using URL_for as the source</li>
<h3>Known Issues</h3>
<li>Login form is not functional</li>

<h2>Validators
</h2>
HTML -
<a href="https://validator.w3.org/nu/#textarea">W3C HTML Validator</a>
CSS -
<a href="https://jigsaw.w3.org/css-validator/">W3C CSS Validation Service, Jigsaw</a>
JavaScript -
<a href="https://jshint.com/">JSHint</a>
Python
<a href="http://pep8online.com/">PEP8 Online</a>

<h1>Credits</h1>
<ul>
<li>Review data and images is taken from from <a href="https://global.techradar.com/">tech-radar</a> </li>

<li>code institute lectures provided all the knowledge needed to build this project and my mentor dbenga helped alot along the way</li>
</ul>
