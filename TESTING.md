# Testing #

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
        When the Remove button is clicked, the selected lesson is removed from the booking, and the booking summary is updated.
        When the Clear Booking button is clicked. All lessons are removed from booking 'bag'. Booking - not booked page is displayed.
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Checkout Page

    User stories being tested: As a User, I expect to purchase lesson/s in a safe and secure way by using card method payments. As a User, I want to be able to make quick purchases for lesson/s by using previously saved personal information.
    Owner story being tested: To be able to provide a secure payment method for my clients/website users
    Test:
        Add lesson to booking
        Try to click on the 'Make a Payment' button
        Try to submit the form with incorrect email address (missing @)
        Try to submit the form without providing a card number
        Add Stripe Test card information and click the 'Make a Payment' button
    Results:
        Button is blocked until the user will provide all required information
        Form shows an error with wrong incorrect email address style
        Error message displayed by Stripe
        After successful test payment, the Payment Success Page / Checkout Success page is displayed
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Checkout Success Page

    User story being tested: As a User, I want to receive email confirmations after I successfully purchased my lesson/s.
    Test:
        Select one lesson to purchase
        Book/add selected lesson to booking
        Fulfill information if not logged in to account
        Provide card details
        Click the 'Make a Payment' button
    Results:
        After successful payment user is transferred to the Checkout Success page
        Email is not sent. The view hasn't got a function to send an email to a user after successful payment
    Verdict:
        Email function added to the view
        Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Contact Page

    User story being tested: As a User, I want to be able to contact the owner/lesson/s provider, so I can ask questions or write an additional query about their services.
    Test:
        Try to send an empty contact form
        Try to enter an incorrect email address, without '@'
        Try to send the form with all required fields
        Check the pre-populated fields when the user is authenticated
    Results:
        After trying to send an empty contact form, validation is showing an error message on the required field
        After trying to send the form with an incorrect email address, validation is showing an error about the wrong email address
        Form send properly, Success messages displayed
        When a user is authenticated, the Full name and Email address fields are auto-populated
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

My Bookings
Active / Archived Booking Pages - Booking Review Page

    User story being tested: As a User, I want to be able to view my ordering history.
    Test:
        Click on the navigation Account link
        Choose one booking from 10 Recently Booked
        From the dropdown user menu click on Active in My Bookings menu section
        From dropdown user menu click on Archived in My Bookings menu section
        Click on booking user want to display
    Results:
        If the user is logged in Account Page is displayed, otherwise, user is transferred to the login page
        After logging in user is navigated to the Account Page where 10 latest orders are displayed
        After clicking on active booking user is transferred to the Order Review page where all booking information is displayed. Including purchased lessons and details button to view lesson details
        After clicking on the Active link in My Booking, a table with active bookings is presented. If the user booked any lessons. Otherwise, information with button navigating to Lessons Page is displayed
        After clicking on the Archived link in My Booking, a table with archived bookings is presented. If the user hasn't got any archived bookings, a Page with information and the button 'View Active Booking' is displayed. If there is no Active Booking then information with a button navigating to the Lessons Page is displayed like in the previous case.
        After clicking any active or archived booking user is transferred to the Order Review page with all important information and lessons booked
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Account Page

    User stories being tested: As a User, I want to be able to login back anytime. As a User, I want to be able to fully changed my personal details, home address, name (in case I'm married now), phone number, e-mail address, etc.
    Test:
        Click on the Account link when not logged in
        Click on the Loggin link
        Try to Loggin in with empty input fields
        Try to Loggin in with an incorrect password
        Try to Loggin in with the wrong email address
        Try to Loggin with correct credentials
    Results:
        After clicking on the Account link user is transferred to Login Page
        Loggin form validation system is displaying error messages
        When all credentials are correct, the user is returned to the page he was currently displaying/viewing.
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Authentication pages (Allauth)

    User stories being tested: As a User, I want to be notified when I successfully finished the registration process. As a User, I want to be able to create my own account, which will give me the possibility to store, view, and edit my profile information. As a User, I want to be able to change my password from my profile account, in case my account was hacked, to protect my personal details.
    Test:
        Click on the Register link
        Click on the Login link
        Click on Forgot Password link
        Click on Logout
        Try to Loggin in with empty input fields
        Try to Register with empty input fields
        Try to Loggin in with incorrect credentials
        Try to Loggin in with an incorrect password
        Try to register with two different passwords
        Try to register with the same existing username
        Try to Loggin in with the wrong email address
        Try to Register with a wrong email address
    Results:
        Register page with the registration form is displayed
        Login page with login form is displayed
        Password reset page with reset form is displayed
        When the logout link is clicked, the user is transferred to Home Page and a success message is displayed
        All different combinations of Try's created an error with messages displayed in forms and Django-messages.
        When Successfully logged into account success message is displayed
        When a user successfully registered, he is transferred to Account page to fulfill details
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Management/Administration (CRUD)

    Admin & Owner stories being tested: To have the possibility to Add, Edit, and Delete lesson/s. To have a secure admin interface, easy to use. Important thing is, this interface must be available only for admins.
    Test:
        Try to access the administration page without login into the account
        Try to access the administration page with a basic user account
        Try to access the administration page with superuser account
        Click on each Management and Home section link from the dropdown menu after the user is logged in (superuser)
        Click on each Remove Button on the selected Lesson, Instructor Profile, or Resort element
        Click on each Edit Button on the selected Lesson, Instructor Profile, or Resort element
        Click on each Add + button on each Administration page
        Trying to Add/Edit selected element with empty random required fields
        Trying to Add/Edit selected element with all required fields filled
    Results:
        When a user is not logged in, the Django-allauth decorator is preventing from accessing the page by navigating the user to the Administration Login page
        When a user is logged in with a standard user account, the Django-allauth decorator is preventing from accessing the page by navigating the user to the Administration Login page
        When a user is logged in with superuser account, Administration/Management page is displayed
        All links are pointing superuser to correct Administration/Management page
        Remove functionality works as expected. By clicking Remove button all instance is removed including images if assigned to.
        When the Edit button is clicked super user is navigated to the Edit Form Page of the selected instance
        When Add + button is clicked super user is navigated to Add Form page of the selected instance
        When Add/Edit form is submitted and required fields are not placed or have incorrect format validation system is showing messages and the form is not submitted until all criteria match.
        When Add/Edit form is submitted and required fields are correctly filled in form is submitted. The instance is added or edited and updated in the database
    Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

Validators
HTML

All the HTML files were validated by using online code validator W3C HTML Validation Service. Errors found were about IMG 'height, width' attributes missing. Wrong code scope by using UL and DIV's, also duplicated ID's were found. Code was checked and all errors and warning were corrected, code is valid with no errors and warnings on all pages.
CSS

All the SCSS and Main.min.css files were validated by using an online code validator W3C CSS Validation Service. There were several errors and warnings found. There are warnings for color contrast according to the background that can be ignored. Also, there are warnings about -WebKit- as validator is catching it as 'an unknown vendor extension'.
JavaScript

All the JavaScript files were validated by using an online code validator Beautifytools.com. Missing semicolons were added at the end of functions. 'Const' and 'Let' warning can be ignored. Validator is showing the message 'is available in ES6 (use 'version: 6') or Mozilla JS extensions (use Moz).' all Const's and Let's will be converted to Var's my browser. Code is syntactically valid. For more information about Const, Let, and Future JS you can use BabelJS
Python

All Python files were validated by using an online code validator Pep8. File changes were made to make the code PEP8 compliant where possible.
Debug = True

While developing an app, the local debugger: debug=True was on. Every time when the application has an error, the debugger was displaying an error message page. Thanks to that I could catch all errors and fix them straight away.
Compatibility and Responsiveness

This website had been being tested during the development in Safari Browser by Web Development Tools.

Mostly I've used Web Inspector and Responsive Design Mode to preview different webpages across various screen sizes, orientations, and resolutions, as well as custom viewports and user agents.

It has also been tested on different browsers such as Google Chrome or Mozilla Firefox.

I have used a powerful online screen resizer and responsiveness tester BlueTree Screenfly Strongly recommended for everyone who wants's easily test responsivity
Bugs
Bugs During Development
