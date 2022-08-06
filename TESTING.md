# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)


Testing was performed with a desktop computer and iphone.
The following browsers were tested:
Google Chrome,
Microsoft Edge
iOS Safari

## Test Case 001

### Python Validation
I checked my code was in line with pep8 and here is this to confirm. The Python code was checked using the pep8 validator available at [pep8online.com](https://pep8online.com). No errors were reported by the validator in the files I created. The settings.py file did however, contain errors for lines too long due to these being environment variables and template tags etc etc I found for the purpose of readability to leave longer, with a warning.

I ran all of these files below through the validator for pep8 guidelines.
The apps I did this for are as follow :
* Candy Cave
* Blog
* Basket
* Checkout
* Home
* Profiles
* Sweets

I Screeshotted me using a online pep8 validator for the Main Sweets and also the Candy Cave main app.

* Screenshots of the validator reports are here:
   
![Test Case 0001](/static/docs/testing_screenshots/tc001.png)

## Test Case 001a

### JavaScript Validation
I used a Javascript validator to ensure that my JavaScript is written correctly and conforms to the correct standards that JavaScript asks for, I used the Jshint.com validator available at [jshint.com](https://jshint.com/). No errors were detected within the files I created. 

    * JavaScript

![Test Case 0001a](/static/docs/testing_screenshots/tc001a.png)

## Test Case 001b

### CSS Validation

The CSS Validator/Prefixer that I used is to ensure that my CSS is compatible with all devices that may use the site. [This is the site that I used](https://autoprefixer.github.io/). When validating by URL it discovers a total of 98 warnings relating to relating to style rules that were written correctly but not necessarily how the CSS file would like to see them. The Warnings are allowed warnings for the CSS due to them only being warnings and not errors.

![CSS AutoPrefixer](/static/docs/testing/css_prefixer.png)

![Test Case 001b](/static/docs/testing_screenshots/tc00b.png)

## Test Case 001c

### HTML Validation
Due to the way Django uses template tags within different files {% #### %} it is not possible to simply just copy the code over from one file to another due to the way Django renders its templates. Therefore when validating the HTML I had to inspect the pages as raw HTML and then copy and post it over into the validator. This ensured that the code that I had written was correct and up to the correct standards.

When validating the pages using their URL the validator return three warnings relating to the type attribute being unnecessary for javascript resources. All of these warnings can be disregarded and aren't an issue to the code.

I was also with an error I noticed during validation that I found was due to the fact that there was no “alt” attribute assigned to the Mail Chimp, I Added my own “alt” attribute, and the error now doesn't exist.

Along with a fault due to the error for the Stripe payment.

![Test Case 001c](/static/docs/testing_screenshots/tc001c.png)

## Test Case 002

![Test Case 002](/static/docs/testing_screenshots/tc002.png)

### Unregistered User Testing - General Site Navigation
The overall site navigation consisted of me manually testing the site and navigating my way around it to ensure that all my views and everything is rendering to the site correctly. This part of my testing was done without being an authorized user.


## Test Case 003

![Test Case 003](/static/docs/testing_screenshots/tc003.png)

### Unregistered User Testing - General Site Navigation - Sweet shop Pages
On the Sweet sites shopping page I also ensure that the navigation was correct I also ensured that only correct information is displaying to the individual sweet view (ie only sweets that can be bought in measurement will only show the measurement field to the user)


## Test Case 004

![Test Case 004](/static/docs/testing_screenshots/tc004.png)

### Unregistered User Testing - Blog Page
The forum/blog pages were also tested to ensure that the functionality of the blog page worked and that information again was being rendered correctly to the screen. And to ensure that the page will not allow you to post unless you are logged in.


## Test Case 005

![Test Case 005](/static/docs/testing_screenshots/tc005.png)

### Unregistered User Testing - Blog Page - individual page
The forum/blog pages' individual blog view was also tested to ensure that this part of the site was only able to the users that are logged in. IE in this test I had to make sure that I wasn't actually able to get to the creation of a blog and that it redirected me to the signup/login page.


## Test Case 006

![Test Case 006](/static/docs/testing_screenshots/tc006.png)

### Registered User Testing - Blog Page - individual page
The Registered user testing view is important to test to make sure that ONLY the user that is logged in and that it is the user that created the blog can then use basic CRUD functionality on it and can read/edit and delete should they wish to do so.

## Test Case 007

![Test case 007](/static/docs/testing_screenshots/tc007.png)

### Unregistered User Testing - Purchase Process
I also checked the site to ensure that with a failed payment method that the site told the user and the site also ensure that the site didnt break after the faulty payment method>

## Test Case 008

![Test Case 008](/static/docs/testing_screenshots/tc008.png)

### Registered User Testing - Make Address Default Process
I also wanted to test the Registered user's Profile/Information update functionality to ensure that registered users always were able to add their information and store it on their account. I had to make sure that from doing so on the payment page added to the profile, plus vise versa

## Test Case 009

![Test Case 009](/static/docs/testing_screenshots/tc009.png)

### Registered User Testing - Delete Address Process
I also wanted to make sure the basic crud functionality of the sites user delete address worked.


## Test Case 009a

![Test Case 009a](/static/docs/testing_screenshots/tc009a.png)

### Contact us Form
I also had on the site in the About page there is a contact us form. This used a basic model to take the users email and for them to then recieve an email. I can confirm that this form works.


## Test Case 010

![Test Case 010](/static/docs/testing_screenshots/tc010.png)

### Registered User Testing - Blog Page
Testing was also carried out when a registered user and the template doesnt change but when clicking the "Add Blog" button it allows the user to the form to create a post.
