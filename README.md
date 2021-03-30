# Dark Luna #

## Private Practice for Holistic Sexuality for Woman ##

![Header Image](/readmecontent/logo.png)

- [Project goals](#project-goals)
- [UX](#ux)
  - [User Goals](#user-goals)
  - [Scope](#scope)
- [Structure of the website](#structure-of-the-website)
  - [View for a guest user](#view-for-a-guest-user)
  - [View for logged in user](#view-for-logged-in-user)
  - [User Stories](#user-stories)
  - [Site owner goals](#site-owner-goals)
- [User Requirements and Expectations](#user-requirements-and-expectations)
  - [Requirements](#requirements)
  - [Expectations](#expectations)
- [Design Choices](#design-choices)
  - [When and why i've diverted from the wireframes](#when-and-why-i've-diverted-from-the-wireframes)
  - [Colors](#colors)
  - [Fonts](#fonts)
  - [Icons](#icons)
  - [Structure](#structure)
- [Wireframes, Flowcharts and Data Models](#wireframes--flowcharts-and-data-models)
  - [Wireframes](#wireframes)
  - [Data Models](#data-models)
    - [Database Structure](#database-structure)
- [Features](#features)
  - [Features that are implemented](#features-that-are-implemented)
  - [The Big Struggle](#the-big-struggle)
  - [Features to be implemented](#features-to-be-implemented)
  - [Known issues](#known-issues)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Tools](#tools)
- [Testing](#testing)
  - [Testing user stories](#testing-user-stories)
- [Manual testing](#manual-testing)
  - [From validating](#from-validating)
- [Bugs](#bugs)
  - [In development](#in-development)
  - [From peer code review](#from-peer-code-review)
  - [From friends and family testing](#from-friends-and-family-testing)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
- [Credit](#credit)
  - [Image credits](#image-credits)
  - [Special thanks](#special-thanks) 
  

## Project goals ##

Supply a website that woman who have hormonal related issues, like problems with fertility, menstruation and sexuality and more general life questions can go to and get information and book appointments for sessions so they can start getting healthier again.

## UX ##

### User Goals ###

- The website has to work well on all kind of devices like mobile phones, tables and desktops
- The login procedure should be clear and feedback should be given when appropriate
- The registration process should be clear, easy to do and feedback should be given when appropriate
- The website has to be easy to use and easy to update information
- Visually appealing website

### Scope ###

An easy to navigate and responsive website that is fun to use and allows users as well as site owners, to perform CRUD operations. Users can sign up and, once logged in, the can either buy products or book appointments. These users manage their purchases and bookings, meaning they can edit and delete them when they want.
Also, they can update their password and username and even delete their account.

## Structure of the website ##

### View for a guest user ###

A user that is not logged in and/or registered, will see a homepage with information about the various sessions that are offered, workshops that will be given and a shop where session related products can be bought. They will also see a sign in and sign up button.
On all pages where services or products are offered, they are prompted to register/login to benefit from these futures. They can also subscribe to a newsletter.

### View for logged in user ###

A logged in user will benefit from the full functionality of the site. The navigation will contain extra: 'Logout'.
This user is able to book appointments, book workshops and buy products they might need for exercises given in sessions.
In the profile there are also functions for changing once username, password and even delete their account.

### User Stories ###

Because there are many user stories for this project, I have made a spreadsheet containing different levels of users (client and user) as well as the stories for the shop owner.
This fill is by no means complete. During development there might be some added or removed, depending on functionality and usability.

View the stories [here](https://github.com/byIlsa/luna/blob/master/readmecontent/userandsiteownerstories.pdf).

### Site owner goals ###

See ["User Stories"](#user-stories)

## User Requirements and Expectations ##

### Requirements ###

- Easy to navigate by using buttons
- Appealing account page with a functional overview
- Easy way to book an appointment or workshop
- Easy way to buy products
- Ability to edit and delete a bookings
- Ability to contact the site owner

### Expectations ###

- When you have booked a session, it should be easy to change or reschedule this appointment.
- To have a account page that has a clear overview of products I have bought and/or appointments I have made.
- It should be easy to book an appointment and/or shop for products.

## Design Choices ##

I have decided on a clean, but playful look and feel for this project. There are many images, short texts with read more options and video's to support the textual content.
WIP

### When and why i've diverted from the wireframes ###

WIP

### Colors ###

I have chosen the following colours I have taken from the logo to support the connection between the logo and the site itself:

#580c2d for headers and titles
#15020a for the company name and body texts
#79113F for section backgrounds
#ffffff for body background

I have used [Coolors](https://coolors.co/) for creating a color scheme.

![Color scheme](/readmecontent/darklunacolours.png)

I have used a contrast checker in order to make sure that the contrast is sufficient. This way my content will be easily readable.

### Fonts ###

For headers, titles and company name: [Oregano](https://fonts.google.com/specimen/Oregano?preview.text=&preview.text_type=custom)

For body text:
[Open Sans](https://fonts.google.com/specimen/Open+Sans?preview.text_type=custom)

Fonts are from [Google Fonts.](https://fonts.google.com/)

### Icons ###

Icons used are from [Font Awesome.](https://fontawesome.com/) The are used in moderation and match the colors and overall feel of the design.

[Shopping bag](https://fontawesome.com/icons/shopping-bag?style=solid)

[Account icon](https://fontawesome.com/icons/user-circle?style=solid)

### Structure ###

For the structure I have used [Bootstrap.](https://getbootstrap.com/)

## Wireframes, Flowcharts and Data Models ##

WIP

### Wireframes ###

For wireframing I have used [LucidChart](https://www.lucidchart.com/pages/)

View my wireframes:

[Mobile](/readmecontent/mobile.pdf)

[Tablet and desktop](/readmecontent/tabletdesktop.pdf)

### Data Models ###

Data models can be viewed here. WIP

#### Database Structure ####

WIP
During the development, I worked with sqlite3 databases, installed with Django. For production I have used [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql).

* The User model I have used in this project was provided by Django Allauth. It is a part of default django.contrib.auth.models.

## Profile app ##

| Name                 | Database Key         | Field Type           | Validation                                                      |
|----------------------|----------------------|----------------------|-----------------------------------------------------------------|
| User                 | user                 | OneToOneField 'User' | on_delete=models.CASCADE                                        |
| Full Name            | full_name            | CharField            | max_length=200, null=True, blank=True                           |
| First Name           | first_name           | models.CharField     | max_length=100, null=True, blank=True                           |
| Last Name            | last_name            | models.CharField     | max_length=100, null=True, blank=True                           |
| Email Address        | email_address        | models.EmailField    | max_length=254, null=False, blank=True                          |
| Phone Number         | phone_number         | models.CharField     | max_length=20, null=True, blank=True                            |
| Street Address 1     | street_address1      | models.CharField     | max_length=80, null=True, blank=True                            |
| Street Address 2     | street_address2      | models.CharField     | max_length=80, null=True, blank=True                            |
| Postcode             | postcode             | models.CharField     | max_length=20, null=True, blank=True                            |
| Town or City         | town_or_city         | models.CharField     | max_length=40, null=True, blank=True                            |
| County               | county               | models.CharField     | max_length=80, null=True, blank=True                            |
| Country              | country              | CountryField         | blank_label='Select Country', null=True, blank=True             |
| Receiving Newsletter | receiving_newsletter | models.CharField     | max_length=3, choices=newsletter_choices, blank=True, null=True |



## Features ##

### Features that are implemented ###

- Registration functionality
- Log In and Out functionality 
-
-
- CRUD Functions:
  - Create:
  - Read:
  - Update:
  - Delete:

### The Big Struggle ###

Might not be needed

### Features to be implemented ###

WIP

### Known issues ###

WIP

## Technologies used ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JS](https://nl.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Frameworks ###

- [Font Awesome](https://fontawesome.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)
- [jQuery](https://jquery.com/)

### Tools ###

- [Git](https://git-scm.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [LucidChart](https://www.lucidchart.com/pages/)
- [PEP8](http://pep8online.com/)
- [W3C HTML Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Github](https://github.com/)
- [Firefox](https://www.mozilla.org/nl/firefox/all/)

## Testing ##

The site was tested by using the LightHouse function for Chromium Developer Tools. A report can be found [here]()

### Testing user stories ###

## Manual testing ##

All manual testing was done using Chromium Developer Tools and testing on an iPhone 11 and an iPad Pro.

Home

Register

Log In

### From validating ###

- Python code has been validated for pep8 compliance with [pep8 validator](http://pep8online.com/)
- HTML code has been validated with [HTML validator](https://validator.w3.org/nu/)
- CSS code has been validated with [CSS validator](https://jigsaw.w3.org/css-validator/)
- JS code has been run through [Esprima](https://esprima.org/index.html)

## Bugs ##

### In development ###

Name

- Bug description:

- Fix:

- Verdict:

### From peer code review ###

### From friends and family testing ###

## Deployment ##
Dark Luna was developed using the GitPod online IDE and using Git & GitHub for version control.
It is hosted on the Heroku platform, with static files and images being hosted in AWS S3 Basket.
### Local Deployment ###

To be able to run this project, the following tools have to be installed:

* An IDE of your choice (I used GitPod for creating this project)
* Git
* PIP
* Python3

Apart from that, you also need to create accounts with the following services:

* Stripe
* AWS to setup the S3 basket
* Gmail

To clone the project:

* You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:

``` git clone https://github.com/byIlsa/Dark-Luna ```

Alternatively, you can save a copy of this repository by clicking the green button Clone or download , then Download Zip button, and after extract the Zip file to your folder.

In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).

Note: You can read more information about the cloning process on the GitHub Help page.

* Set up environment variables.

Note, that this process will be different depending on IDE you use.

In this it was done using the following way:

* Create .env file in the root directory. 
* Add .env to the .gitignore file in your project's root directory 
* In .env file set environment variables with the following syntax:

        import os  
        os.environ["DEVELOPMENT"] = "True"    
        os.environ["SECRET_KEY"] = "<Your Secret key>"    
        os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
        os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
        os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"

 
Read more about how to set up the Stripe keys in the Stripe Documentation.

* Install all requirements from the requirements.txt file putting this command into your terminal:

``` pip3 install -r requirements.txt ```

* In the terminal in your IDE migrate the models to crete a database using the following commands:

``` python3 manage.py makemigrations ```

``` python3 manage.py migrate ```

* Load the data fixtures(list of fixtures) in that order into the database using the following command:

``` python3 manage.py loaddata <fixture_name> ```

* Create a superuser to have an access to the admin panel(you need to follow the instructions then and insert username, email and password):

``` python3 manage.py createsuperuser ```

* You will now be able to run the application using the following command:

``` python3 manage.py runserver ```

* To access the admin panel, you can add the /admin path at the end of the url link and login using your superuser credentials.

## Heroku Deployment

To start Heroku Deployment process, you need to clone the project as described in the Local deployment section above.

To deploy the project to Heroku the following steps need to be completed:

* Create a requirement.txt file, which contains a list of the dependencies, using the following command in the terminal:

``` pip3 freeze > requirements.txt ```

* Create a Procfile, in order to tell Heroku how to run the project, using the following command in the terminal:

``` web: gunicorn dark_luna.wsgi:application```

* git add, git commit and git push these files to GitHub repository.

NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but illustrated here as they are required for the successful deployment to Heroku.
As well as that, other things that are required for the Heroku deployment and have to be installed: gunicorn (WSGI HTTP Server), dj-database-url for database connection and Psycopg (PostgreSQL driver for Python).
All of the mentioned above are already installed in this project in the requirements.txt file.

* On the Heroku website you need to create a new app, assign a name (must be unique),set a region to the closest to you(for my project I set Europe) and click Create app. 
* Go to Resources tab in Heroku, then in the Add-ons search bar look for Heroku Postgres(you can type postgres), select Hobby Dev — Free and click Provision button to add it to your project. 
* In Heroku Settings click on Reveal Config Vars. 
* Set the following config variables there: 

| KEY                  | Value    | 
| :-------------       | :---------- | 
|AWS_ACCESS_KEY_ID     | your aws access key  | 
|AWS_SECRET_ACCESS_KEY | your aws secret access key |
|DATABASE_URL          |  your postgres database url|
|EMAIL_HOST_PASS       |  your email password(generated by Gmail)|
|EMAIL_HOST_USER       |  your email address|
|SECRET_KEY            |  your secret key|
|STRIPE_PUBLIC_KEY     |  your stripe public key|
|STRIPE_SECRET_KEY     |  your stripe secret key|
|STRIPE_WH_SECRET      |  your stripe wh key|
|USE_AWS               |  True|
|

* Copy DATABASE_URL's value(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in settings.py.

You can temporary comment out the current database settings code and just paste the following in the settings.py: 
```DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")
    }
```
Important Note:

That's just temporary set up, this URL should not be committed and published to GitHub for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.

* Migrate the database models to the Postgres database using the following commands in the terminal:

``` python3 manage.py makemigrations ```

``` python3 manage.py migrate ```

* Load the data fixtures(list fixtures) into the Postgres database using the following command:

``` python3 manage.py loaddata <fixture_name> ```

* Create a superuser for the Postgres database by running the following command(you need to follow the instructions and inserting username, email and password):

``` python3 manage.py createsuperuser ```

* You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.

Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.

* Add your Heroku app URL to ALLOWED_HOSTS in the settings.py file.

* You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.

To do so, from the Heroku dashboard follow the steps:

* Deploy section -> Deployment method -> select GitHub 
* Link the Heroku app to your GitHub repository for this project 
* Click Enable Automatic Deploys in the Automatic Deployment section 
* Run git push command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.

Alternatively, in the terminal you can run:

``` heroku login -i ```

* After adding and committing to Git, run the following command:

``` git push heroku master ```

* After successful deployment, you can view your app bu clicking Open App on Heroku platform. 
* You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!

Hosting media files with AWS

The static files and media files (that will be uploaded by superuser - product/service images) are hosted in the AWS S3 Bucket. To host them, you need to create an account in AWS and create your S3 basket with public access. More about setting it up you can read in Amazon S3 documentation and this tutorial.

Sending email via Gmail

In order to send real emails from the application, you need to connect it to your Gmail account, setting up your email address in EMAIL_HOST_USER variable and your app password generated by your email provider in EMAIL_HOST_PASS variable.

## Credit ##

Credits
    • Texts are all created by myself or the client who wrote the testimonials.

### Image credits ###

Favicon generated with: [Favicon generator](https://www.favicon-generator.org/)

### Special thanks ###

- My Yoda-mentor [Simen Daehlin](https://github.com/Eventyret) for being there when I lost my way and didn't know how to get back. And for being the kick-ass person that he is.

- Everybody at Slack for their support, tips and humor!

For his undying love and support and always being there, my love, you know who you are ;)

**Site for educational purposes only!**
