# Dark Luna #

## Private Practice for Holistic Sexuality for Woman ##

![Header Image](/wireframes/logo.png)

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
- [Wireframes and Data Models](#wireframes-and-data-models)
  - [Wireframes](#wireframes)
  - [Data Models](#data-models)
- [Features](#features)
  - [Features that are implemented](#features-that-are-implemented)
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

An easy to navigate and responsive website that is fun to use and allows users as well as site owners, to perform CRUD operations. Users can sign up and, once logged in, the can book a workshop and add comments to the blogs. These users manage their comments and bookings, meaning they can edit and delete them when they want.

## Structure of the website ##

### View for a guest user ###

A user that is not logged in and/or registered, will see a homepage with information about the various sessions that are offered, workshops that will be given, a page where they can 'meet' the therapists and a blog. They will also see a sign in and sign up option in the navigation.
On all pages where services  are offered, they are prompted to register/login to benefit from these futures. They can also subscribe to a newsletter in the footer.

### View for logged in user ###

A logged in user will benefit from the full functionality of the site. The navigation will contain extra: 'Logout'.
This user is able to book workshops and and add comments to blog posts.
In the profile the can see and change their personal information and view the latest booked workshops.

### User Stories ###

This file is by no means complete. During development there might be some added or removed, depending on functionality and usability.

| as a/an…    | I want to be able to…                                       | So that I can…                                                                         |
|-------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------|
|             |                                                             | Viewing and navigation                                                                 |
| User        | General                                                     |                                                                                        |
|             | easily navigate the site on mobile, Desktop and tablet      | so I can quickly decide if this is something I would like to use                       |
|             | Find information about what the mission Of this company is  | so I can see if this feels right for me                                                |
|             | Sessions                                                    |                                                                                        |
|             | see what therapy options are offered                        | decide what kind of session I would like to book                                       |
|             | Workshops                                                   |                                                                                        |
| user        | see what workshops are offered                              | decide if I would like to participate in a workshop                                    |
| client      | book a workshop                                             | so i can participate                                                                   |
| user        | see details about a workshop                                | so i can see what it is all about                                                      |
|             | Blog                                                        |                                                                                        |
| user/client | read blog posts                                             | so I get informed about topics I’m interested in                                       |
| client      | add/edit/delete comments                                    | so i can tell what I am thinking and feeling                                           |
|             |                                                             | Sorting and Searching                                                                  |
|             | Workshop general                                            |                                                                                        |
| User        | Sort the list of workshops                                  | See workshops by name or price                                                         |
|             | Sort for specific category                                  | Find workshops in a specific category or sort The products in that category by  name   |
|             | Search for workshops by name or description                 | Find a specific product I’d like to purchase                                           |
|             | Easily see what I’ve searched for and the Number of results | Quickly decide whether the workshop I want is available                                |
|             |                                                             | Bookings, purchase and checkout                                                        |
| Client      | Workshop booking                                            |                                                                                        |
|             | Easy to follow payment procedure                            | So I can book without spending much time figuring out how                              |
|             | View bookings in my bag                                     | So I can see what I’ve booked and what the total cost is                               |
|             | Enter my payment info easily                                | Check out quickly without problems                                                     |
|             | Have my information stored secure                           | Rest assured my personal info is safe                                                  |
|             | Get an order confirmation after checkout                    | Keep a copy for future reference/waranty                                               |
|             |                                                             | Registration and User Accounts                                                         |
| User        | Easily register for an account                              | Have a personal account                                                                |
|             | Easily login or logout                                      | Access my personal account information                                                 |
|             | Easily recover my password in case I forgot                 | Recover access to my account                                                           |
|             | Receive an email confirmation after  Registering            | Verify that my account registration was successful                                     |
| Client      | Have a personalized account page                            | View my personal order history and order confirmations and save My payment information |
|             | See what bookings I’ve made                                 | get an overview of my bookings                                                         |
|             |                                                             | Subscription                                                                           |
| User        | easily register for a newsletter                            | so I can receive news when it becomes available                                        |
|             |                                                             | Admin and Store management                                                             |
| Store owner | Add a workshop                                              | Add new workshops to my store                                                          |
|             | Edit a workshop                                             | Edit workshops                                                                         |
|             | Delete a workshop                                           | Delete a workshop                                                                      |
|             | delete/edit blog posts                                      | delete and/or edit blog posts                                                          |
|             | Add blog posts                                              | add blog posts                                                                         |
|             | add/edit/delete workshop categories                         | manage workshop categories                                                             |
|             | add/edit/delete therapists                                  | manage new therapists arriving and/or therapists leaving the practice                  |

### Site owner goals ###

See ["User Stories"](#user-stories)

## User Requirements and Expectations ##

### Requirements ###

- Easy to navigate by using buttons
- Appealing account page with a functional overview
- Easy way to book a workshop
- Ability to edit and delete a booking
- Ability to contact the site owner

### Expectations ###

- Registering for an account should be no fuss.
- To have a account page that has a clear overview of products I have bought and/or appointments I have made.
- It should be easy to book a workshop.

## Design Choices ##

I have decided on a clean, but playful look and feel for this project. There are many images, short texts with read more options and video's to support the textual content.
WIP

### When and why i've diverted from the wireframes ###

I have decided to not have seperate pages for sex, life and shadowwork. There wasn't that much text and for faster browsing and easier reading, I decided to condence them into one app; 'Coaching'.

I decided to leave the shop part out. Instead I focussed on selling workshops. Reasons being, there aren't that many products connected to the site (yet).

I ended up not having a big header on all pages. I decided it would be an eye catcher on the index, but let the other content talk for itself on the other pages and use colours to brighten them up.

### Colors ###

I have chosen the following colours I have taken from the logo to support the connection between the logo and the site itself:

I have used [Coolors](https://coolors.co/) for creating a color scheme.

![Color scheme](/wireframes/darklunacolours.png)

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

## Wireframes and Data Models ##

Wireframes where created at the very beginning of this project and have been followed for as much as possible.

### Wireframes ###

For wireframing I have used [LucidChart](https://www.lucidchart.com/pages/)

View my wireframes:

[Mobile](/wireframes/mobile.pdf)

[Tablet and desktop](/wireframes/tabletdesktop.pdf)

### Data Models ###

During the development, I worked with sqlite3 databases, installed with Django. For production I have used [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql).

- The User model I have used in this project was provided by Django Allauth. It is a part of default django.contrib.auth.models.

## Profiles app ##

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

## Workshops app ###

### Category Model ###

|      Name     |  Database Key | Field Type |               Validation               |
|:-------------:|:-------------:|:----------:|:--------------------------------------:|
| Name          | name          | CharField  | max_length=254                         |
| Friendly Name | friendly_name | CharField  | max_length=254, null=True, blank=False |

### Workshop Model ###

| Name         | Database Key | Field Type                   | Validation                                             |
|--------------|--------------|------------------------------|--------------------------------------------------------|
| Name         | name         | models.CharField             | max_length=254                                         |
| Description  | description  | models.TextField             | null=True, blank=True                                  |
| category     | category     | models.ForeignKey 'Category' | null=True, blank=False, on_delete=models.CASCADE       |
| Start Date   | start_date   | models.DateField             | null=True, blank=False                                 |
| End Date     | end_date     | models.DateField             | null=True, blank=False                                 |
| Start Time   | start_time   | models.TimeField             | auto_now=False, auto_now_add=False                     |
| End Time     | end_time     | models.TimeField             | auto_now=False, auto_now_add=False                     |
| Participants | participants | models.IntegerField          | null=True, blank=False                                 |
| Price        | price        | models.DecimalField          | max_digits=6, decimal_places=2, null=True, blank=False |
| Image        | image        | models.ImageField            | upload_to="user_uploads", null=True, blank=True        |
| therapist    | therapist    | models.CharField             | max_length=254                                         |

## Blog app ##

### Blog Model ###

| Name         | Database Key | Field Type        | Validation                                |
|--------------|--------------|-------------------|-------------------------------------------|
| Title        | title        | models.CharField  | max_length=255                            |
| Tag          | tag          | models.CharField  | max_length=255                            |
| Author       | author       | models.ForeignKey | User, on_delete=models.CASCADE, null=True |
| header_image | header_image | models.ImageField | null=True, upload_to="user_uploads/"      |
| Body         | body         | models.TextField  | blank=True, null=True                     |
| post_date    | post_date    | models.DateField  | auto_now_add=True                         |
| Snippet      | snippet      | models.CharField  | max_length=166                            |
| likes        | likes        | models.ManyToMany | max_length=255, blank=True                |
| source       | source       | models.CharField  | max_length=255, blank=True                |

### Blog Commments ###

| Name       | Database Key          | Field Type           | Validation                                              |   |
|------------|-----------------------|----------------------|---------------------------------------------------------|---|
| post       | post                  | models.ForeignKey    | Post, related_name="comments", on_delete=models.CASCADE |   |
| name       | name                  | models.ForeignKey    | User, on_delete=models.CASCADE, null=True               |   |
| body       | body                  | models.TextField     |                                                         |   |
| date_added | database Keyate_added | models.DateTimeField | auto_now_add=True                                       |   |

## Therapists app ##

| Name  | Database Key | Field Type        | Validation                                   |
|-------|--------------|-------------------|----------------------------------------------|
| Name  | name         | models.charField  | max_length=200, null=True, blank=False       |
| About | about        | models.textField  | null=True, blank=False                       |
| Image | image        | models.imageField | upload_to=”therapist”, null=True, blank=True |

## Features ##

### Features that are implemented ###

- Registration functionality
- Log In and Out functionality
- Booking (workshops)
- Sign Up for newsletter (MailChimp)
- Contact site owner
- Have a profile page
- Moon Calendar
- Blog (with comments section)

- CRUD Functions:
- Create:
  - Account (profile)
  - Comment to blog
  - Contact form content
  - Workshops
  - Add therapist

- Read:
  - Account (profile)
  - General info (sessions, massage, workshops, therapists, blog)

- Update:
  - Account(profile)
  - Bookings
  - Comments
  - Blog Posts
  - Therapists information

### Features to be implemented ###

I would like to add a testimonials app. I have been working with that, but time sadly did not permit me to make a fully CRUD funtioning app of it.
There should also be an option to add/edit and delete categories to the blog section. Again, I have been working on it, but it was using a slug url and I couldnt figure out how to use this to create the edit/delete function. Also everytime I added a new category, the server needed to be restarted. I need more time to figure this one out before feeling ready to implement this. And as this project is e-commerce centered, I decided to abandon this function for a later date.

### Known issues ###

There have been many struggles concerning the back-end. Namly the function to get an email to send after a booking has been confirmed. I had that working, with the help of a tutor. I pushed the code and went to bed, feeling very relieved, because stripe webhooks have been known to cause a headache or two.
I woke up the following morning and returned to the project, to find out the webhook had yet again failed. I asked tutor support again and spend no less that five hours with a different tutor, troubleshooting. Unfortunately we werent able to figure out what was wrong (code was valid). So I ended up removing the whole code for sending a email.

Unfortunately this particular problem has cause me to loose a lot of valuable time, forcing me to choose between other functionality or beauty, I choose the first. I was adament to get all functionality working as intended and I did (for the most part). But it took it's toll on the front end, something I still am gutted about.

The project is not fully responsive and could use some major improvements on some area's. There is overflow coming from the body elemement. I did spend a considerable amount of time to try and find out where it was coming from, but the deadline prevented me from investigating any further.

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
- [Gimp](https://www.gimp.org/)

## Testing and Bugs ##

Testing and Bug information can be found in a seperate file - [Testing.md](https://github.com/byIlsa/Dark-Luna/blob/master/TESTING.md)

## Deployment ##

Dark Luna was developed using the GitPod online IDE and using Git & GitHub for version control.
It is hosted on the Heroku platform, with static files and images being hosted in AWS S3 Basket.

### Local Deployment ###

To be able to run this project, the following tools have to be installed:

- An IDE of your choice (I used GitPod for creating this project)
- Git
- PIP
- Python3

Apart from that, you also need to create accounts with the following services:

- [Stripe](stripe.com/)
- [AWS](aws.amazon.com/) to setup the S3 basket
- [Gmail](http://mail.google.com/mail?hl=nl)
- [MailChimp](https://mailchimp.com/)

To clone the project:

- You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:

``` git clone https://github.com/byIlsa/Dark-Luna ```

Alternatively, you can save a copy of this repository by clicking the green button Clone or download , then Download Zip button, and after extract the Zip file to your folder.

In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).

Note: You can read more information about the cloning process on the GitHub Help page.

- Set up environment variables.

Note, that this process will be different depending on IDE you use.

In this it was done using the following way:

- pip install python-dotenv
- Add .env to the .gitignore file in your project's root directory
- In .env file set environment variables with the following syntax:

DEVELOPMENT=development
SECRET_KEY=secret key
STRIPE_PUBLIC_KEY=secret key
STRIPE_SECRET_KEY=secret key

STRIPE_WH_SECRET=secret key

EMAIL_HOST_USER=secret
EMAIL_HOST_PASSWORD=secret

DATABASE_URL=database url

AWS_ACCESS_KEY_ID=secret key
AWS_SECRET_ACCESS_KEY=secret key
AWS_S3_CUSTOM_DOMAIN=s3 url

- Add the following to your settings.py

```from dotenv import load_dotenv```
```load_dotenv()```

- Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys).

Call your variables either with os.getenv() or os.environ.get()
In settings.py:
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = "DEVELOPMENT" in os.environ

Note that DEBUG will be True if there's a DEVELOPMENT key/value pair in your .env file, regardless of
its value (i.e. if it has any value it will be True).
This means that DEBUG will be False in production, unless the DEVELOPMENT variable is added to the
production host's environment variables.
Don't forget to add .env to your .gitignore and never track it with version control!

- Install all requirements from the requirements.txt file putting this command into your terminal:

``` pip3 install -r requirements.txt ```

- In the terminal in your IDE migrate the models to crete a database using the following commands:

``` python3 manage.py makemigrations ```

``` python3 manage.py migrate ```

- Create a Procfile, in order to tell Heroku how to run the project, using the following command in the terminal:

```web: gunicorn dark_luna.wsgi:application```

- git add, git commit and git push these files to GitHub repository.

NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but illustrated here as they are required for the successful deployment to Heroku.
As well as that, other things that are required for the Heroku deployment and have to be installed: gunicorn (WSGI HTTP Server), dj-database-url for database connection and Psycopg (PostgreSQL driver for Python).
All of the mentioned above are already installed in this project in the requirements.txt file.

- On the [Heroku](heroku.com/) website you need to create a new app, assign a name (must be unique),set a region to the closest to you(for my project I set Europe) and click Create app.
- Go to Resources tab in Heroku, then in the Add-ons search bar look for Heroku Postgres(you can type postgres), select Hobby Dev — Free and click Provision button to add it to your project.
- In Heroku Settings click on Reveal Config Vars.
- Set the following config variables there:

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
|MAILCHIMP_API_KEY     |  Your API Key|
|MAILCHIMP_AUDIENCE_ID | Your audience Key|

- Copy DATABASE_URL's value(Postgres database URL) from the Convig Vars and temporary paste it into the default database in settings.py.

You can temporary comment out the current database settings code and just paste the following in the settings.py:

```python
  DATABASES = {
    'default': dj_database_url.parse("your Postgres database URL here")
  }
  ```

Important Note:

That's just temporary set up, this URL should not be committed and published to GitHub for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.

- Migrate the database models to the Postgres database using the following commands in the terminal:

``` python3 manage.py makemigrations ```

``` python3 manage.py migrate ```

- Load the data fixtures in this specific order, because one relies on the other (categories, workshops, therapists, comments, blog) into the Postgres database using the following command:

``` python3 manage.py loaddata <fixture_name> ```

- Create a superuser for the Postgres database by running the following command (you need to follow the instructions and inserting username, email and password):

``` python3 manage.py createsuperuser ```

- You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.

Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.

- Add your Heroku app URL to ALLOWED_HOSTS in the settings.py file.

- You can connect Heroku to GitHub to automatically deploy each time you push to GitHub. But be aware that if you use AWS to host your static and media files, automatic deployment may result in being billed if you are on a free account.

To do so, from the Heroku dashboard follow the steps:

- Deploy section -> Deployment method -> select GitHub
- Link the Heroku app to your GitHub repository for this project
- Click Enable Automatic Deploys in the Automatic Deployment section
- Run git push command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.

Alternatively, in the terminal you can run:

``` heroku login -i ```

- After adding and committing to Git, run the following command:

``` git push heroku master ```

- After successful deployment, you can view your app by clicking **Open App** on Heroku platform.
- You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!

Hosting media files with AWS

The static files and media files (that will be uploaded by superuser - product/service images) are hosted in the AWS S3 Bucket. To host them, you need to create an account in AWS and create your S3 basket with public access. More about setting it up you can read in [Amazon S3 documentation](https://docs.aws.amazon.com/s3/index.html) and [this](https://www.youtube.com/watch?v=e6w9LwZJFIA) tutorial.

Sending email via Gmail

In order to send real emails from the application, you need to connect it to your Gmail account, setting up your email address in EMAIL_HOST_USER variable and your app password generated by your email provider in EMAIL_HOST_PASS variable.

MailChimp

- First, of all you need to Sign up and create your account at [MailChimp](https://mailchimp.com/). Go to the MailChimp website to register your website.

  - Fill up your details or credentials of your and your website and finally activate your account from the mail they sent you.

- Create an Audience

  - After complete registration with MailChimp, you will land to the Dashboard of MailChimp.

  - Now we have to create an Audience. So click on the Audience button in the right hand side menu bar. Then click signup forms in the yellow bar, then click Embedded Forms.

  - Now fill up your all necessary details in the Embedded Forms section. These details may be included in the MailChimp emails you sent, so If you have any hosted email service, use that email address. After you successfully filled up your details, click on Save.

- Get Your Audience and API KEY

  - After creating your List, get your List Key and API key.

  - You can get your Audience Key from audience > settings
  - Scroll down the page, you fill find a field of Unique id for ```<your audience name>```. Copy your audience id from there.

  - After that, get your API key from Account > Extras > API Keys. Then click on Create a Key button to get your API key.

## Credit ##

Credits
    • Texts that are not credited under the text (blog items) are created by myself.

### Source credits ###

[Moon Calendar](http://www.wdisseny.com/lluna/?lang=en)

The Blog app was created by following this video. I changed it to suit my needs.

[Blog app](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)

### Image credits ###

All images are taken from: [Unsplash](unsplash.com/), except:

[Yoniflower](https://img.culturacolectiva.com/content/2013/10/Las-vaginas-mas-bellas-del-mundo.jpg)

[wanderingeye](https://saidadesilets.com/how-to-take-advantage-of-your-mans-wandering-eyes/)

Favicon generated with: [Favicon generator](https://www.favicon-generator.org/)

Logo created by myself and someone who would like to remain anonymous. I used [Gimp](https://www.gimp.org/) for the finishing touches.

### Special thanks ###

- My Yoda-mentor [Simen Daehlin](https://github.com/Eventyret) for being there when I lost my way and didn't know how to get back. And for being the kick-ass person that he is.
- Fellow student [Karol Sliwka](https://github.com/KarolSliwka) for his [Arctic school](https://github.com/KarolSliwka/ArcticSchool) project, from whom I've learned a lot!
- Everybody at Slack for their support, tips and humor!

For his undying love and support and always being there, my love, you know who you are ;)

**Site for educational purposes only!**
