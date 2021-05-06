# Testing #

- [Manual testing](#manual-testing)
  - [Responsiveness](#responsiveness)
  - [Navigation](#navigation)
  - [Home Page](#home-page)
  - [Coaching Page](#coaching-page)
  - [Massage Page](#massage-page)
  - [Workshops Page](#workshops-page)
  - [Workshop Detail Page](#workshop-detail-page)
  - [Booking Page (bag icon in navigation)](#booking-page--bag-icon-in-navigation-)
  - [Checkout Page](#checkout-page)
    - [Checkout Success Page](#checkout-success-page)
  - [Blog Page](#blog-page)
  - [Therapists Page](#therapists-page)
  - [Contact Page](#contact-page)
  - [Account page (icon in navigation)](#account-page--icon-in-navigation-)
- [Validators](#validators)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Debug = True](#debug---true)
- [Compatibility and Responsiveness](#compatibility-and-responsiveness)
- [Bugs](#bugs)
  - [In development](#in-development)

## Manual testing ##

### Responsiveness ###

- User story being tested: As a User, I want to easily navigate the site on mobile, Desktop and tablet.

  - Test:
    - Each page of the website was created based on a mobile-first responsive web design approach, next on tablets and desktop devices
    More information about responsiveness testing can be found in Compatibility and Responsiveness section
    - Results: Small issues, to name a view: Columns wrong size for specified breakpoint. Font-size wrong size.
  - Verdict: The issues were fixed as far as time permitted, the test passed.

### Navigation ###

- User story being tested: As a User, I want to easily navigate the site on mobile, Desktop and tablet.
  - Test:
    - Click on each link in the navigation to see, if they're pointing the user to the correct page
    - Check if navigation is changing links to the 'hamburger button' on tablets and mobile devices when resizing
    - Check if navigation is fixed/show on the top of the page on each page when scrolled down - all devices
    - Click the Account icon when the user is not logged in to the user account to see the 'Login', 'Register' buttons on the dropdown menu
    - Click the Account icon when the user is logged in to see the standard user 'Profile' section (name of logged in user is showing) with Active / Archived Booking button and Logout Button
    - Click the Account icon when Super User is logged in to see all standard user links plus blog, categories, workshops, therapists admin links
    - Click all links in different dropdown menu's to seeif the point to the right pages and have the correct styles applied
    - Click on the Dark Luna logo - link to see, if the user will be navigated to Home Page
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Home Page ###

- User stories being tested: As a User, I Find information about what the mission Of this company is, see what therapy/workshop options are offered.
  - Test:
    - Scroll down on Home Page to see, if all information is displayed correctly and easy to read.
    - Click on all links provide on the Home page and see if they lead to the correct pages.
    - Click on the blog links to see if the lead to the correct blog page detail - page.
    - Add an email address in the footer to check if it submits correctly to mailchimp.
  - Results:
    - All information is present and pleasantly presented, leading to the correct pages.
    - Adding an emailaddress to the footer has lead to a sign up with success email from MailChimp.
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Coaching Page ###

- User stories being tested: As a User, I want see what therapy options are offered.
  - Test:
    - Click on the Coaching Page link
    - Click the 'Why' and 'How' links provided on this page
- Results:
  - All information is present and displayed
  - Links working as expected
- Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Massage Page ###

- User stories being tested: As a User, I want see what therapy options are offered.
  - Test:
    - Click on the Massage Page Link
- Results:
  - All information is present and displayed
- Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Workshops Page ###

- User stories being tested: As a User, I want see what workshops are offered, book a workshop, sort the list of workshops, sort for specific category, Ssarch for workshops by name or description.
  - Test:
    - Click on the Workshops Page Link
    - Search icon clicked/enter button pressed when the field is empty
    - Search icon clicked/enter button pressed when the field is not empty
    - Click on All Workshops Buton
    - Click on a Category button
    - Change filtering option
    - Click the 'details button'
    - Clcik the 'book now button'
  - Results:
    - All available workshops displayed
    - When the search field is empty an error message is displayed; 'Please enter a valid search criteria'.
    - When the search field isn't empty search term is displayed below search box. Workshops matching the search term are displayed.
    - When the All Workshops button is clicked, all workshops are presented on page
    - When Category link is clicked only workshops matching clicked category are presented
    - When All Workshops or Single Category is chosen and filtering option is applied page is showing workshops in the correct order
    - All clicked buttons lead to correct pages.
  - Verdict: Tests passed, works as expected, after bug fix during testing. Functionality covered.

### Workshop Detail Page ###

- User stories being tested: As a user, I want to see details about a workshop.
  - Test:
    - Click on the 'Details' button
  - Result:
    - Clicking the button leads to the correct page and all is displayed as expected
  - Verdict:
    - Tests passed, works as expected, after bug fix during testing. Functionality covered.
- User stories being tested: As a user, I want to be able to book a workshop.
  - Test:
    - Click on the 'book now' button.
  - Result:
    - Button triggers a window to be displayed, informing the user that the workshop has been added to the bag. This window also gives the user the opportunity to go directly to the secure checkout page. The price of the workshop is being displayed beneath the bag icon. Clicking the bag icon gives the user a review of the booked workshop with additional options (edit/delete).
  - Verdict:
    - Tests passed, works as expected, after bug fix during testing. Functionality covered.

### Booking Page (bag icon in navigation) ###

- User story being tested: As a User, I want to View bookings in my bag.
  - Test:
    - No workshops booked
    - Add one workshop to the booking
    - Add more than one workshop to booking
    - Click on the Details button of booked workshops
    - Click on the Remove button of the selected workshop
    - Click on the Clear Booking button
- Results:
  - Display Booking Page - no workshops booked
  - Booking summary information displayed such as Booking total and grand Total
  - One workshop displayed on Booking Page with all information such as price, name and therapist
  - Basic information is displayed for each workshop when more than one booked, Booking summary updated
  - When the details button clicked, the user is redirected to the selected workshop details page 'Workshop Page'
  - When the Remove button is clicked, the selected workshop is removed from the booking, and the booking summary is updated.
  - When the Clear Booking button is clicked. All lessons are removed from booking 'bag'. Booking - not booked page is displayed.
- Verdict: Tests passed, works as expected, bug on remove button found and solved. Functionality covered.

### Checkout Page ###

- User stories being tested: As a User, I expect to enter my payment info easily, have my information stored secure, get an order confirmation after checkout
  - Test:
    - Add workshop to booking
    - Try to click on the 'Secure Checkout' button
    - Try to submit the form with incorrect email address (missing @)
    - Try to submit the form without providing a card number
    - Add Stripe Test card information and click the 'Make a Payment' button
  - Results:
    - Button is blocked until the user will provide all required information
    - Form shows an error with wrong incorrect email address style
    - Error message displayed by Stripe
    - After successful test payment, the Payment Success Page / Checkout Success page is displayed
- Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

#### Checkout Success Page ####

- User story being tested: As a User, I want to Get an order confirmation after checkout
  - Test:
    - Select one workshop to purchase
    - Book/add selected workshop to booking
    - Fulfill information if not logged in to account
    - Provide card details
    - Click the 'Make a Payment' button
  - Results:
    - After successful payment user is transferred to the Checkout Success page
    - Order confirmation is displayed on the screen. If the user is logged in, this summary is also displayed on the profile page
  - Verdict:
    - Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Blog Page ###

- User story being tested: As a user, I want to read blog posts and add/edit/delete my personal comments and like a post
  - Test:
    - Click the Blog link in the navigation
    - Click the Read More button on a blog post
    - Click the like button
    - Click the unlike button
    - Click the add comment button
    - Write a comment
    - Edit that comment
    - Delete that comment
    - View number of likes and comments
  - Result:
    - Clicking all the buttons above produced the wanted result
    - Adding a comment succeeded and comment was added to blogpost
    - Edit and delete function only visible for user who has wrote that comment
    - Those functions produced the desired result
    - Unlike button only visible when user has liked the post. Like button only visible if user did not like the post (yet)
    - Viewing of likes and comments works as expected and adds and subtrackts whenever the appropriate buttons are clicked.
  - Verdict:
    - Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

- Store owner story being tested: As a store owner I would like to edit and delete my blog posts (adding will be covered in the account page section)
  - Test:
    - Log in as superuser
    - Navigate to Blog Page
    - Click the details button on a blog post
    - Edit or delete a blog post
  - Result:
    - Edit and delete links only appear if the logged in user is also the blog poster.
    - Editing and deleting a blog post works and gives correct feedback when appropriate.
  - Verdict:
    - Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Therapists Page ###

- User story being tested: Not existing in user stories. Last minute addition.
  - Test:
    - Click the therapists link in navigation
    - View page
  - Result:
    - Clicking on the link redirects the user to the correct page and the information is being displayed.
  - Verdict:
    - Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Contact Page ###

- User story being tested: As a User, I want to be able to contact the owner.
  - Test:
    - Try to send an empty contact form
    - Try to enter an incorrect email address, without '@'
    - Try to send the form with all required fields
    - Check the pre-populated fields when the user is authenticated
  - Results:
    - After trying to send an empty contact form, validation is showing an error message on the required field
    - After trying to send the form with an incorrect email address, validation is showing an error about the wrong email address
    - Form send properly, Success messages displayed
    - When a user is authenticated, the Full name and Email address fields are auto-populated
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Account page (icon in navigation) ###

Personal Information - Booking Review Page

- User story being tested: As a User, I want to have a personalized account page where I can view my personal information and update them and see what bookings I’ve made
  - Test:
    - Click on the navigation Account icon
    - Choose to view either Personal info or Workshops
    - Click on booking user want to display
  - Results:
    - If the user is logged in Account Page is displayed, otherwise, user has options for login or register
    - After logging in user is navigated to the Account Page two buttons, Personal Information and Workshops are being shown
    - After clicking the Personal Information button, a dropdown is shown with the correct information and an option to update the info
    - After clicking the Workshops button, a dropdown is shown with either no information or links to booked workshops. Clicking the booking number shows the booking review page
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Login/Register

- User story being tested: As a User, I want to easily register for an account, easily login or logout, easily recover my password in case I forgot, receive an email confirmation after Registering
  - Test:
    - Click on the Account icon when not logged in
    - Click on the Login link
    - Try to Login in with empty input fields
    - Try to Login in with an incorrect password
    - Try to Login in with the wrong email address
    - Try to Login with correct credentials
  - Results:
    - After clicking on the Account icon user is presented with the login and register links
    - Clicking either of them redirects them to the correct form
    - Login form validation system is displaying error messages
    - When all credentials are correct, the user is returned to the homepage and a successmessage is shown.
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Page when SuperUser (CRUD)

- Site owner stories being tested: As a site owner, I would like to add/edit/delete a workshop, add/edit/delete a workshop category, add a blog post and add/edit/delete therapists
  - Test:
    - When a superuser is logged in, additional functions become active (Blog, Categories, Workshops and Therapists)
    - Clicking either of them should lead to an Admin page or directly to the add blog page.
    - Try to access the administration page without login into the account
    - Try to access the administration page with a basic user account
    - Try to access the administration page with superuser account
    - Click on each Admin link
    - Click on each Add  button on each Admin page
    - Trying to Add/Edit selected element with empty random required fields
     -Trying to Add/Edit selected element with all required fields filled
  - Results:
    - All links point to the correct page and that page gives the correct options for adding, editing and deleting blog, category, workshop and therapists.
    - All forms are validated and give an appropriate message when submitting.
    - When a user is not logged in, the Django-allauth decorator is preventing from accessing the page by navigating the user to the Administration Login page
    - When a user is logged in with a standard user account, the Django-allauth decorator is preventing from accessing the page by navigating the user to the Administration Login page
    - When a user is logged in with superuser account, Administration/Management page is displayed
    - All links are pointing superuser to correct Admin page
    - Remove functionality works as expected. By clicking Remove button all instance is removed including images if assigned to.
    - When the Edit button is clicked super user is navigated to the Edit Form Page of the selected instance
    - When Add button is clicked super user is navigated to Add Form page of the selected instance
    - When Add/Edit form is submitted and required fields are not placed or have incorrect format validation system is showing messages and the form is not submitted until all criteria match.
    - When Add/Edit form is submitted and required fields are correctly filled in form is submitted. The instance is added or edited and updated in the database
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

## Validators ##

### HTML ###

All the HTML files were validated by using online code validator W3C HTML Validation Service. Errors found were about Jinja templating, sections missing headers and two instances where the aria-controles on the account and workshop buttons had incorrect values.
A warning was given regarding MailChimp code: ```Warning: The type attribute for the style element is not needed and should be omitted.```.
For the booking app, there where some errors saying there where unclosed div's. I checked the code, but could not find any. More like these where found, I wish I could solve them, but time did not give me any room for a search.

### CSS ###

All the CSS files were validated by using an online code validator W3C CSS Validation Service. There were several errors and warnings found. There are warnings for font-weights not having the right value (450 when 400 was expected). Also, there are warnings about -WebKit- as validator is catching it as 'an unknown vendor extension'.

### JavaScript ###

All the JavaScript files were validated by using an online code validator JSHint.com. Missing semicolons were added at the end of functions. 'Const' and 'Let' warning can be ignored. Own code is syntactically valid, in the how.js file there were some warnings I tried to fix. ``` Missing '()' invoking a constructor. (W058)jshint(W058) ``` I looked this one up and found out this is something in the linter that doesnt need fixing [article](https://github.com/jshint/jshint/issues/1357)

### Python ###

All Python files were validated by using an online code validator Pep8. File changes were made to make the code PEP8 compliant where possible.

## Debug = True ##

While developing an app, the local debugger: debug=True was on. Every time when the application has an error, the debugger was displaying an error message page. Thanks to that I could catch all errors and fix them straight away.

## Compatibility and Responsiveness ##

This website had been being tested during the development in FireFox. using Web Development Tools.

Mostly I've used Web Inspector and Responsive Design Mode to preview different webpages across various screen sizes, orientations, and resolutions, as well as custom viewports and user agents.

It has also been tested on different browsers.

I have used a powerful online screen resizer and responsiveness tester [BlueTree Screenfly](bluetree.ai/)

## Bugs ##

### In development ###

Name: Add blog post not working

- Bug description: When adding a blog post from the front end, the add button returns an error ```Reverse for 'blog-post-detail' with arguments '('2', '6')' not found. 1 pattern(s) tried: ['blog/article/(?P<pk>[0-9]+)$']```
It did however post the addition. It turns out I was only one comma away :)

- Fix: in models.py ```return reverse('blog-post-detail', args=(str(self.id),))``` added a comma between the closing parenthesis and it worked.

- Verdict: All good!

Name: Order comfirmation emails not being printed to the console

- Bug description: When going through the secure checkout procedure, I discovered that there wasnt any indication that an order comfirmation was send upon successfull checkout. Further investigation revealed that there wasnt any data send back from the webhook, at all. With the help of Igor from tutor support I discovered that I had a type in my url handling (/webhook instead of /wh).

- Fix: Fixing that, (and subsequent some additional errors in the field handling between the webhook_handlers and the fields in stripe.js), fix the problem.

- Unfortunately this did not make it to production. The webhook proofed to be very unreliable and was throughing tantrums on and off. After more than 10 hours of tutor support, I decided to remove the function as it was not mandatory.

- Verdict: Removed.

Name: Grand_total not being showed in order review

- Bug description: In the order review that is generated after a successfull checkout, the grand_order_total is not displayed.

- Fix: Forgot to put ```default_app_config = 'checkout.apps.CheckoutConfig'``` in the _init_.py of the checkout app. So there was nothing listening to the signals.

- Verdict: All good!

Name: Template post mortem for error message

- Bug description: When an error was made when filling out a form, the error message was not showing. I checked and double checked everything and then posted it on slack. Thankfully, I was made aware that the correct file format is error.htmL and not error.htm. Classic case of fatigue and code blindness. Gotta love the slack community!

- Fix: Put an L in the file format. Sometimes it is really that simple.

- Verdict: All good!

Name: Sorting of workshop categories not working

- Bug description: When testing this function, I noticed the whole function did not do anything. Oops!

- Fix: This function needs JavaScript to work. So I added the JavaScript, and it worked!

- Verdict: All good!

Name: Remove item from bag not working

- Bug description: When testing this function, I noticed that the button had no function attached

- Fix: Added the correct class to the button and then it worked.

- Verdict: All good!
