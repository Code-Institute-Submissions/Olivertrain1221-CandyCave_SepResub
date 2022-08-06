# Candy Cave

## Introduction

Candy Cave shop is a website built using the framework Django and using languages such as Python, Javascript, HTML and CSS. The site is a fully functioning ECommerce site for a fictional shop called “Candy Cave” The shop is aimed to be a modern take on an old school sweet shop during the “disco earer” the idea is the user can navigate the site and find sweets and get them added to a basket and delivered to there door. With all the niceties of a fully functioning shop.
The users are able to select different measurements of sweets in grams and are then able to also order 2 lots of seperate 100g this is perfect for someone who likes a variation or may even be thinking of doing a gift bag etc etc.

The site also shows reviews left by valid customers which is important for the site to be successful as a ecommerce store.

This is the fifth project for the Code Institute Diploma in Software Development with eCommerce.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, Full CRUD functionality for approved users for Products, Categories, Blog Posts and Categories along with Reviews and Responses.

![Screenshot of homepage](/static/docs/site-images/home_desktop.png)

[View the live website on Heroku](https://candycave.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
- [Candy Cave](#candycave)
  * [Introduction](#introduction)
  * [Table of Contents](#table-of-contents)
  * [UX](#ux)
    + [Overall Goals](#overall-goals)
    + [The Strategy Plane](#the-strategy-plane)
    + [The Sites Ideal User](#the-sites-ideal-user)
    + [Site Goals](#site-goals)
    + [Epics](#epics)
    + [User Stories](#user-stories)
    + [The Scope Plane](#the-scope-plane)
    + [The Structure Plane](#the-structure-plane)
    + [The Skeleton Plane](#the-skeleton-plane)
      + [Wireframe mock-ups](#wireframe-mock-ups)
      + [Database Schema](#database-schema)
      + [SEO Considerations](#seo-considerations)
  * [The Surface Plane](#the-surface-plane)
  * [Features](#features)
  * [Future Enhancements](#future-enhancements)
  * [Social Media](#social-media-marketing)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## UX

### Overall Goals
* To provide an ecommerce solution for a small business selling sweets to consumers - B2C
* To enable business employees to maintain and update the site content in line with their needs easily.
* To provide users with a simple product selection and purchase experience.

<br>

### The Strategy Plane
* Candy Cave is a business to consumer B2C ecommerce site for users. The overall design of the site is intended to provide users with a clean and easy to navigate environment whilst providing the level of detail required for the different types of products.

### The Sites Ideal User
* Sweet enthusiast searching for any sweets they may of had on the past and try new.
* Someone looking to gift someone.

### Site Goals

* To provide users with a place to purchase their sugary needs
* To promote the product range of sweets Candy Cave has on the market
* To provide easy navigation with a fun theme to entice all ages in

### Epics
5 Epics were created which were then further developed into 15 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/Olivertrain1221/CandyCave/issues)

1. Initial Django setup [#1](https://github.com/Olivertrain1221/CandyCave/issues/1)
2. Fulfilling the sites intention and build as a shop [#2](https://github.com/Olivertrain1221/CandyCave/issues/2)
3. Account Functionality [#3](https://github.com/Olivertrain1221/CandyCave/issues/3)
4. Account Login/Logout [#4](https://github.com/Olivertrain1221/CandyCave/issues/4)
5. Users Shopping Basket [#5](https://github.com/Olivertrain1221/CandyCave/issues/5)

### User Stories

From the Epics,I developed 15 user stories; however I feel that more were required for the size of the site that this is. From the stories that I did create I managed to nearly complete them all however due to the time constrains regarding my lack of experience with Django, Plus the time required to plan and design the project. I was unable to complete a few or the stories.

The stories also consisted of tasks within the stories due to me finding that a suitable user story required multiple elements in order to satisfy the overall picture. I found by adding the tasks that I was able to then successfully complete the stories and ensure that i had thought of the bigger picture.

1. Navigation Around the Site [#1](https://github.com/Olivertrain1221/CandyCave/issues/6)
2. Clear Pricing [#2](https://github.com/Olivertrain1221/CandyCave/issues/7)
3. Login To My Account [#3](https://github.com/Olivertrain1221/CandyCave/issues/8)
4. Product Accessibility [#4](https://github.com/Olivertrain1221/CandyCave/issues/9)
5. Pre-populate the site with products [#5](https://github.com/Olivertrain1221/CandyCave/issues/10)
6. Responsive Templates [#6](https://github.com/Olivertrain1221/CandyCave/issues/11)
7. Can Delete there Profile [#7](https://github.com/Olivertrain1221/CandyCave/issues/12)
8. Deployment to Heroku [#8](https://github.com/Olivertrain1221/CandyCave/issues/13)
9. Logout [#9](https://github.com/Olivertrain1221/CandyCave/issues/14)
10. Add to Basket [#10](https://github.com/Olivertrain1221/CandyCave/issues/15)
11. Wish List [#11](https://github.com/Olivertrain1221/CandyCave/issues/16)
12. Payment [#12](https://github.com/Olivertrain1221/CandyCave/issues/17)
13. Email Order Confirmation [#13](https://github.com/Olivertrain1221/CandyCave/issues/18)
14. Contact Us [#14](https://github.com/Olivertrain1221/CandyCave/issues/19)
15. Product Display [#15](https://github.com/Olivertrain1221/CandyCave/issues/20)

**Features planned:**
*User Profile - Able to Create, Read, Update and Delete
*User Address - Able to Create, Read, Update and Delete
*User Login Details - Password Update/Change/Reset
* Users can logout of their account
* Sweet items - Create, Read, Update and Delete
* Sweet Search - by category and keyword
* Sweets individually- View product details or summary information
* Shopping basket - Add, Update and Remove products from the shopping basket
* Checkout - Enter delivery information and payment information
* Payment Processing - Successfully process payment information and confirm orders
* Order Confirmation - Confirm order information on payment success
* Blog - Create, Read, Update and Delete
* Email newsletter subscription - Ability to subscribe to a company newsletter for marketing purposes.
* Contact Us - Ability for all users to contact the company directly.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access it


### The Structure Plane
<br>
#### Initial Setup
As a Developer, I can setup Django and install the supporting libraries needed for my E-Commerce Project, so that I am ready to start development

<br>

#### Implementation:
Install Django
Install required libraries, external and internal packages
Create requirements file to track dependencies
Create the first app

<br>

#### Secure the Keys 
As a Developer, I want to setup the Django environment to secure the secret keys, so that I do not expose the keys in an insecure way

<br>

#### Implementation:
Create an env.py file to store the environment variables
Amend Django to point to the new location for the secret keys
Add the env.py file to the .gitignore file so that it does not get pushed to GitHub
Deployment - As a Developer, I want to deploy the app to Heroku, so that I can confirm everything works before development of the site and to enable continuous testing within the production environment

<br>

#### Create a new Heroku app
Add the database to the app resources
Add the secret key's to the Heroku config vars
Configure the settings.py file to point at the correct env.py file in development, the os in deployment and adjust the database section to point at the correct database url from Heroku in deployment
Add the Amazon AWS S3 bucket details to the env.py file and to the Heroku config vars. Access Key and Secret Access Key.
Add the email user details and password to the env.py file and to the Heroku config vars
Add the stripe details to the env.py file and to the Heroku config vars. Public key, secret key and wh-secret

<br>

#### SEO 
As a Site Owner, I would like The site to have all the content needed to perform well in SEO, so that ultimately the site has the ability to perform well in search results and can be found

<br>

#### Acceptance Criteria
Given that the site is deployed, When the spiders visit the site, then there is a sitemap to guide them.
Given that content is written for the site, When it is written, then the keyword research is utilized to ensure relevant information is included

<br>

#### Implementation:
Conduct Keyword Research prior to planning out the site
From keyword research plan content requirements for the site
From keyword research plan site content
Create sitemap.xml file utilizing www.xml-sitemaps.com
Place sitemap.xml file in the root directory
Create robots.txt file

<br>

#### Contact Us
As a User, I would like to be able to contact the company prior to making my purchase, so that I can ask them a question about one of the products

<br>

#### Acceptance Criteria
Given that I am a user on the website, When I want to contact the company to ask a question, Then there is an easily accessible method for me to do so

<br>

#### Implementation
Develop a contact form for users to get in touch with the company
Link the form submission with an email system so that messages sent will arrive at the company and can be responded to

<br>

#### Create Blog Post
As a user I would like to be able to share my views on the sweets I buy and be able to read other customers thoughts before I purhcase something.

<br>

#### Acceptance Criteria
Given that I have an account, When I am logged into my account, Then I have the ability to create a new blog post
Given that I am logged into my account, When I navigate to create a new blog post, Then I have a form to fill out to create my blog post
Given that I am a logged in user, When I successfully complete the blog post form and submit it, Then a new blog post is created and published to the site

<br>

##### Implementation
Create blog post model
Create blog post form for employees to add blog posts to the site
Develop validation to ensure that the blog post is completed correctly
Restrict access to blog post form page to users only
Develop backend processes to process the form and publish it to the site

<br>

#### Edit Blog Post
As the User that made the post its important that i can edit the post and delete the post should i maybe change my mind about something I may have said. Super users have the option to remove the item.

<br>

#### Acceptance Criteria
Given that I am a logged in, When I view a blog post, Then I have the option to edit it
Given that I am a logged in, When I select the option to edit a blog post, Then I am taken to a form with the blog post information in it so I can edit the section I want
Given that I am a logged in, When I edit a blog post, Then on submitting the edited form the blog post is updated

<br>

#### Implementation
Develop the option for users to edit blog posts
Develop a form for users to edit the blog post
Develop validation for the form to ensure blog post information is complete

<br>

#### View Blog Post 
As a User, I would like to be able to read blog posts full of useful information, so that I can keep upto date on the company and learn new information

<br>

#### Acceptance Criteria
Given that I am a user on the site, When I navigate to the blog post page, Then I am presented with all the blog posts that are available
Given that I am a user on the blog posts page, When I click on a blog post, Then I am taken to the full post details

<br>

#### Implementation
Develop a blog post page to display all the blog posts
Develop blog post cards to display a summary of each post
Develop a blog post detail page to display the full post
Link the blog card to the detail page for each blog post

<br>

#### Delete Blog Post 
As The user that made the post, I would like to be able to delete a blog post, so that in the event we need to remove one completely we can take it down from the site

<br>

#### Acceptance Criteria
Given that I am a logged in, When I navigate to a blog post, Then I have the option to remove the post
Given that I am a logged in, When I select the remove option on a blog post, Then the post is removed from the site

<br>

#### Implementation
Develop an option in the blog post edit page to delete the post
Develop the functionality to delete the post from the database
Restrict access to the functionality to users

<br>

#### Create Account
As a User, I would like to be able to create an account, so that I don’t have to enter my details every time I place an order

<br>

#### Acceptance Criteria
Given that I am an unregistered user, And, I am on the user registration page, When I enter my email address and password, And, I click on the register button, Then the system creates me an account, And, it tells me that my account has been created
Given that I have an account, And, I have items in my basket, When I navigate to checkout, Then I have my address information ready to be used
Given that I have an account, And, I try to navigate to the register page, When I enter my email address and password, And, I click on the register button, Then the site tells me that I already have an account

<br>

#### Implementation
Develop the ability for users to register for an account
Develop ability for users to save details to their account such as address
Prevent multiple accounts being created for the same email address

<br>

#### Edit Account 
As a User, I would like to be able to edit the details/address stored on the sweet shop, so that If I move, or if I want to use more than one address, I can store them all

<br>

#### Acceptance Criteria
Given that I have a user profile, And, I am logged into my profile, When I navigate to my profile, Then I have the ability to add different addresses on my account
Given that I have a user profile, And I am logged in, When I navigate to my profile, And, I have more than one address stored, Then I can select one to be the default address
Given that I have a user profile, And, I am logged into my profile, When I navigate to my profile, Then I have the ability to edit the addresses
Given that I have a user profile, And, I am logged into my profile, When I navigate to my profile, Then I have the option to delete the addresses

<br>

#### Implementation
Develop the ability for users to save addresses to their profile
Develop the ability for users to set one address as default
Develop the ability for users to edit the addresses on their profile
Develop the ability for users to delete the addresses on their profile

<br>

#### View Account 
As a User, I would like to be able to view the details stored on my account, so that I can review what is stored

<br>

#### Acceptance Criteria
Given that I have a user account, When I am logged into my account, Then I have an option to view my account
Given that I have a user account, And, I am logged in, When I navigate to view my details, Then everything that is stored within my account is available to be viewed
Given that I have a user account, When I navigate to the url to view my account whilst not logged in, Then I am redirected to the login page and i'm unable to view the details without being logged in

<br>

#### Implementation
Develop a link in the menu that takes logged in users to their profile
Develop a link within the user profile page that they can use to view all other information associated with the account - previous orders
Restrict access to account details to logged in users - specifically the user whose details they are

<br>

#### Delete Account 
As a User, I would like to be able to delete my account, so that I have full control over the information that is stored about me

<br>

#### Acceptance Criteria
Given that I have a user account, When I view my account details whilst logged in, Then I have the option to delete my account
Given that I have a user account, And, I am on my account details page, When I select to delete my account, And, I confirm the deletion request, Then my account is deleted

<br>

#### Implementation
On the user profile page provide an option to delete account
Require a second confirmation for account deletion
Develop a method to delete the account when the user requests it to be deleted - will need to keep order history seperate for company records

<br>

#### Account Login
As a User, I would like to be able to login to my account, so that I can access the advantages of having an account

<br>

#### Acceptance Criteria
Given that I am a registered user, When I navigate to the login page, Then I can enter my details to login to my account
Given that I am a registered user, When I navigate to the login page and enter my details, And, I click login, Then I am logged into my account and I am able to see a visual confirmation that I am now logged in
Given that I am a registered user, And, I try to log into my account, When I enter the wrong information, Then the site informs me that the information was incorrect and prevents my logging in

<br>

#### Implementation
Develop a link to a login page
Develop a login form for users to confirm their login details
Develop form validation to ensure the data is entered correctly
Develop a method to validate the data entered matches a user account
Develop a redirect so unlogged in users are redirected to the login page when trying to access pages that require the user to be logged in

<br>

#### Account Logout
As a User, I would like to be able to log out of my account, so that I can keep my account secure

<br>

#### Acceptance Criteria
Provided that the user is logged into the account, When I click on the logout link, Then I am asked to confirm to logout
Given that I am a logged in user who has clicked logout, When I confirm I want to logout, Then I am logged out of my account
Given that I am a registered user, who has signed out of my account, When I use the browser navigation buttons such as back button, Then I cannot access information which requires me to be signed in

<br>

#### Implementation
Develop link for users to access logout functionality</li>
Develop logout confirmation form to log users out</li>
Develop a redirect so if a user signs out whilst on a page requiring a user to be logged in, it redirects them appropriately

<br>

#### Add Products
As an Store Owner, I would like employees to be able to add new products to the site easily, so that the site can be kept up to date with any new sweets.

<br>

#### Acceptance Criteria
Given that I am an employee, When I log into the site, Then I should have additional stock management options available
Given that I am a logged in employee, When I select add product, Then I should be directed to a form that allows me to add a new product to the site
Given that I am a logged in employee, And, I have completed the form to add a product, When I submit the form, Then the new product should appear on the site

<br>

#### Implementation
Develop a separate navigation bar for employee users to allow access to other site areas
Develop a form for employees to add products to the site
Develop validation to ensure that product information is completed correctly
Develop the backend to process the form data and create a new product file/page to be added to the site

<br>

## The Skeleton Plane

<br>

### Wireframe mock-ups
Wireframes were produced for the Majority of ther sites main pages. This helped to develop a theme which i made sure to include on the more redundant pages that wireframes weren't made for (login/logut/contact us forms)[here](/static/docs/wireframes.pdf).

Attention was paid to the elements that would be present on each page such as the header, nav bar  and the footer.
The header allows for multiple levels of navigation around the site and also provides the user with shortcuts to information on the store plus there personal information and is all within the same place throught site navigating. This is important for continuity and fluidity through the site

Home page: The home page provides the user with a Humorous photo of a gummy bear standing up in a pile of gummy bears. Sweets are considered to be fun anyway therefore this I feel helps to give the user a sense of understanding for the website. Not only that but they can see straight away all of the main features of the site on the desktop site. Including sufficient filter methods.

![Home Page Mobile Wireframe](/static/docs/wireframes/home_wireframe_m.png)

<br>

![Home Page Mobile](/static/docs/site-images/home_mobile.png)

<br>

![Home Page desktop Wireframes](/static/docs/wireframes/home_wireframe_d.png)

<br>

![Home Page desktop](/static/docs/site-images/home_desktop.png)

<br>

All Sweets Page: I felt that it was important to display the sweets in a fancy/eye catching way i feel that due to the dark top and vibrant pink writing that the neon green hugh around the card elements draws the user in to each card where the relevant information is being shown for a potential sale for the store.

<br>

![All Products desktop Page wireframe](/static/docs/wireframes/sweet_shop_desktop.png)

<br>

![All Products desktop Page](/static/docs/site-images/shop_desktop.png)

<br>

![All Products mobile Page wireframe](/static/docs/wireframes/sweet_shop_mobile.png)

<br>

![All Products mobile Page](/static/docs/site-images/shop_mobile.png)

<br>

Individual Product Page: For each individual product there are three sections, sometimes four. If the sweet has the ability to be purchased in a measurement of sweet then a filter box is shown for the user to input their requirements.

Shopping Cart: For the shopping cart functionality wireframes were produced for both the page and the preview/confirmation message when a user adds a product to the shopping cart. For the shopping cart it is important to allow users to adjust the items in the cart, increase or decrease individual items quantity or remove items completely.

Checkout: The checkout is a similar layout as to the Boutique Ado styling due to me using the table idea and displaying as I believed this was the ideal display method for the checkout. But I ensured to add my own styling to ensure it incorporated with my site's theme.

Order Confirmation: The Order Confirmation is a similar layout as to the Boutique Ado styling due to me using the table idea and displaying as I believed this was the ideal display method for the order confirmation.But ensured to add my own styling to ensure it incorporated with my sites theme.

All Blog Posts Page: The blog posts page is a key page within the site. This is where any post is displayed similar to the way the card images are displayed for the sweets. This Is a key page due to it potentially bringing sales in for the company via good reviews on the sweets they have supplied.

<br>

![All Blog Posts Page](/static/docs/wireframes/blog_desktop.png)

<br>

![Individual Blog Post Page](/static/docs/wireframes/blog_mobile.png)

<br>

### Database Schema
![Database Schema Diagram](/static/docs/database_planning/scema.png)

<br>

I made Several Custom Models for the site that were required for the site in order to be able to code them. The intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model to help with the basic setup of users interacting with the site. I Fully understand how this works. 

![User and Address Models](/static/docs/database_planning/scema.png)

For the sweets I made a custom model based on the boutique ado walkthrough project however I did add my own fields therefore I feel this is valid as my own view due to the changes and fields added. This was done by adding fields to show the weight of food that they can buy in and this gave the feel of a more filled customer user interface.
A model also allows the user to leave a review/blog on the page to allow them to leave comments on a blog-style forum page. Relating to users creating reviews of products, one to record the user's review.

<br>

### SEO Considerations

<br>

#### Keyword Research
For the site I considered the SEO to be important because why build a great Site and it never be found. This I found important so I researched the SEO and looked for the research of the SEO. Research was conducted to discover the appropriate keywords to utilize given the target that would be searching for the site.

#### UK:

![Sweets](/static/docs/seo_optimisation/sweets.png)

![Candy](/static/docs/seo_optimisation/candy.png)

![Sweet Shop](/static/docs/seo_optimisation/sweet_shop.png)

![Party](/static/docs/seo_optimisation/party.png)

<br>

#### USA:

![Sweets](/static/docs/seo_optimisation/sweets_usa.png)

![Candy](/static/docs/seo_optimisation/candy_usa.png)

![Sweet Shop](/static/docs/seo_optimisation/sweet_shop_usa.png)

![Party](/static/docs/seo_optimisation/party_usa.png)


For the searching of these important key words i used “Semsrush” this was useful in order to help with the finding what words needed to be used to make it worldwide hence the “candy and sweets” also as you can see the “Sweet Shop USA” is a massive low rate in the USA as the term sweet shop isn't used.

<br>

#### Content Strategy
For the Sites SEO strategy i wanted to provide an informative hence the blog and also an ecommerce story the pages that were selling the products had to be informative. The site could have been made a lot easier with just displaying the products without a description page and setting them as tick boxes… Yes it would have also looked awful but the idea of using a description page on each product is it boosts the seo and allows the owners of the site to use more keywords.

## The Surface Plane

<br>

### Design
Once I had then thought of the overall structure and the idea of the logic behind the site. I was able to think around design. My first approach was to the site's color palette. I chose a very vibrant and enjoyable theme as at the end of the day, what people eat sweets and are sad. The color scheme I understand is in your face and I wanted to try to bring a modern take on the old Candy stores as they were colorful. The neon is striking and I feel it pulls the user into the site.

![Color Contrast Grid](/static/docs/database_planning/color_pallette.png)


### Typography 
For Fonts Used i use only 2 different fonts the fonts i utilized were clear and smart and also fitted in with the theme of the overall site. The Index slogan was given a font family of ‘Signika’, sans-serif. This was to make the main slogan stand out and look different. The other font family Iused for the rest of the site was the ‘Bebas Neue’, This I felt added a nice feel and a friendly vibe from the ecommerce store.

<br>

##### Images
I Used some images also for my about page. These were found on [Unsplash](https://unsplash.com/)

![About Image 1](/media/inside_shop.jpg)

![About Image 2](/media/sweet_jars.jpg)

The background image that I used is found in [Pexels](https://www.pexels.com/) The image that I ended up using and chose is below.

![Background image](/media/background.jpg)

<br>

## Features

### Navigation
The site navigation consists of main links to navigate around the site's multiple pages, each page consisting of images and The main navigation is split into two sections. The first section contains the main navigation for the site's main sections of interest.

![Nav-Barr Desktop View](/static/docs/site-images/nav_bar.png)

<br>

### Footer
There are also navigation links at the bottom of my footer which users can access areas of the site, this includes certain things you wouldn't want in the main pages of the site such as the newsletter which is displayed using Mail Chimp I also added a privacy policy

![Footer Desktop View](/static/docs/site-images/footer.png)

### Homepage
The home page greets users with a welcoming site with lots of color; the idea of the homepage is to entice them into the site's awesome features, the homepage has a funny entertaining candy themed food image which runs through the site. There is also an enticing logo message which has a shop now button situated next to it.

<br>

### All Products
The “Sweet Shop” is a shop that has a summary of cards displaying cards for each product the site sells.

![All Products desktop Page](/static/docs/site-images/shop_desktop.png)

<br>

### Product Search
Users can search the site for different products through the search bar which is activated by clicking on the search icon located within the main header.
When a search is completed by the user, the site will then display the items from the result of the search; this is great for searching for your favorite sweet.
The individual product view that shows the individual sweet that the user has clicked on shows the image, title, information, plus an option  if available for that particular item: a measurement of sweet.

![Sweet Card](/static/docs/site-images/individual_sweet.png)

### Add to Basket
When a user adds a product to their basket they receive a confirmation message that it has successfully been added

<br>

### Basket
When the user is happy with what they want or even if it is just a singular purchase, they can then navigate to the basket app which handles displaying all the selected products.

![Basket Page](/static/docs/site-images/basket.png)

### Checkout
When the user is ready to purchase the products that they have selected, they proceed to the checkout page, where they can enter their billing and delivery information. Registered users can save the information they have already entered and create a new address record. This is useful for repeat custom as if it takes them 10-15 minutes each time to buy something when they think about it they probably won't have time. The final part of the form that takes the user's details is the payment details, this is taken directly from Stripe - or inserted by Stripe for the purposes of capturing the payment card information. As the Stripe payment system is not fully activated, only the test card information can currently be utilized.

<br>

It's important to display the users previous orders to the site and it does this on the users profile page this allows the site to show the user what they ordered last time all in one place so they can therefore then make repeat customs due to maybe a sweet they have discovered and really now love.

<br>

### User Account Management
Registered users have the full functionality to update their profile which has their information stored on the site; this makes it a nicer experience for the user to be able to update their previous information should it change. 

![User Info Page](/static/docs/site-images/update_users_info.png)

### Blog
The User blog is a basic blog but due to time restraints I had to work fast due to a successful application for my first developer job. The site currently consists of cards displaying 3 values. The title of the post, the posts information and the author of the post It iterates over this and shows information on the cards of users' thoughts, experiences and the all time favorites.
For further development plans I did plan to link it to the sweets themselves and also to then be able to filter the posts that users posted. However, as mentioned above this was not feasible in the time period.

![Blog Page](/static/docs/site-images/forum.png)


The blog detail page gives the user the full image of the site's post and also if it consists of x amount of characters shows the rest of the information.

![Individual Blog Page](/static/docs/site-images/detail_view.png)

<br>

### Contact Us
A Contact Us page can also be found at the bottom of the about page; this allows the user to send to the company an email which they can then respond to in due course.

![Contact Us Page](/static/docs/site-images/contact_us.png)

<br>

## Future Enhancements
As mentioned in a previous section due to the time constraints the site is not as full as I wished for it to be at the completion stage for this particular project.
* First enhancement I would make would be to link the sweets that the user is leaving a review on that can be linked and tagged to the post itself. 
* I would also like to be able to enhance this further and to be able to only limit certain customers to leave reviews if they are to have purchased that actual product from the site.
* Further enhancements I would also like to include also consist of the site having more pages after completion of a sale the sale of the items then could be put there a tracking model which can then in turn be shared to the user to provide them more information regarding their order.

<br> 

## Social Media Marketing
For the purpose of the assessment for the Code Institute course I had also to show my understanding for the importance for social media due to this i created a “Fake” Facebook page for the site this was linked down in the bottom footer however due to facebook's rules and regulations the live facebook site for the shop was taken down. This therefore caused me to remove the site's link and just have it as an empty link.

![Candy Cave Facebook Page](/static/docs/seo_optimisation/facebook.png))

![Candy Cave Facebook Page Posts](/static/docs/seo_optimisation/facebook_posts.png))

## Testing

### Testing Strategy
I utilized an automated and manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md).
Separate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. The commit at which the functionality requirements for each user story were met is listed in the issues section of the repo. It was applied to each issue before it was closed and marked as completed.

<br>

#### Testing Overview
The Testing for the site was split in to subsections and then down into finer sections to ensure that the site is built correctly and works as designed to do so.

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

<br>

#### Validator Testing
All of my files that I have written code into were tested correctly and ensured to be up to standards. Again this can be found in the above testing folder.
All code passed the validation, with only code generated by other parties producing errors or warnings.
* Django built-in code within the settings file produced five line length errors. 
* Bootstrap code produced 260 warnings in the CSS validation. 
* Fontawesome cdn produced 6 HTML validation errors relating to css variables within the cdn css code. 
* The HTMX library that is inserted into the HTML template by django produces a warning stating that the link does not need to have the javascript file type declared.

<br>

#### Automated Testing
Automated tests were not written for this site however i did plan to the site automated tests were going to be written for the blog and profile apps, the features I had planned to test was to check that the forms and views all worked correctly and as expected to do so.

<br>

#### Lighthouse Testing
I used Google's lighthouse built in feature to chrome to get an overall assessment of the site's setup. Whilst all the areas of the test return a green score above 90 occasionally the performance would drop to 80-85 however I put this down to a weaker internet connection at these times. The SEO score returned a perfect 100.

![Google Lighthouse Results]()

#### Notable Bugs
* Within the blog post page A issue I faced and could work out was due to the fact that the slug was not being correctly passed through or adapted and saved/made for the database once i realized I had to force it to save the slug i used the slugify import to do so.

* I also found an issue during the deployment stage of the project, upon launching to heroku I was aware that it couldn't host images. I decided to use AWS and provide images that way. I was everytime challenged with a invalid token key error.
I checked all my config vars in the heroku app along with also making sure i was relating to them in the projects settings.py file correctly. After then conforming to my AWS buckets and noticing that it was trying to “collect static” but failing at this point on the heroku build.
I then looked deeper into this and found that my user in AWS secret key began with the “=” as a initial character. I ended up restarting the aws start up to get complete new keys and the new user key was a random generated key with a more expected value. I changed the value of this secret key and some others that were required to delete this key in the first place. The site then worked correctly and had images all displaying correctly.

<br>
!
#### Technologies Used

* Python
    * The following python modules were used on this project:
       asgiref==3.5.2
     * astroid==2.9.3
boto3==1.24.37
botocore==1.27.37
certifi==2022.5.18.1
charset-normalizer==2.0.12
click==8.0.3
colorama==0.4.4
defusedxml==0.7.1
distlib==0.3.4
dj-database-url==0.5.0
Django==3.2
django-allauth==0.41.0
django-countries==7.2.1
django-crispy-forms==1.14.0
django-storages==1.12.3
filelock==3.6.0
gunicorn==20.1.0
idna==3.3
isort==5.10.1
itsdangerous==2.0.1
jmespath==1.0.1
lazy-object-proxy==1.7.1
MarkupSafe==2.0.1
mccabe==0.6.1
oauthlib==3.2.0
Pillow==9.1.1
platformdirs==2.4.1
psycopg2==2.9.3
psycopg2-binary==2.9.3
pycodestyle==2.8.0
pylint==2.12.2
python-dateutil==2.8.2
python3-openid==3.2.0
pytz==2022.1
requests==2.28.0
requests-oauthlib==1.3.1
s3transfer==0.6.0
six==1.16.0
sqlparse==0.4.2
stripe==3.5.0
toml==0.10.2
urllib3==1.26.9
virtualenv==20.13.3
Werkzeug==2.0.2
wrapt==1.13.3


* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* HTMX
    * HTMX is a JavaScript library that enables forms to be submitted and data to be retrieved from the backend without refreshing the entire page. It was used extensively for pages that included form submission such as the creation of the recipes where creating ingredients in another model, and creating steps in a third model was required. This package provided a simpler approach to using multiple formsets and custom JavaScript.
* JavaScript
    * Custom JavaScript was utilised to enable the colour scheme functionality, the mobile menu, the enabling and disabling of buttons on forms to prevent users inadvertantly causing errors when trying to submit multiple forms at the same time, and to display the current image in the form rather than a hyperlink to the image itself.
* Bootstrap 5.2
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* Balsamiq was utilised to develop wireframes for the site from which the design was based
* Adobe Illustrator was used to adapt images for use within the site.
* Figma was used to develop the database schema during development - I used this instead of a DB app due to the ease with which to document the actual field types rather than some of the online apps which don't include fields that are available.

#### Resources Used

* The Django documentation was used extensively during development of this project
* The HTMX documentation was used as a reference source for the development of the HTMX features
* The Django AllAuth documentation was used as a reference and a guide for implementing the package and its features.
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


## Deployment

The site was deployed via Heroku, and the live link can be found here - [candycave](https://candycave.herokuapp.com/)

### Project Deployment - needs adapting for AWS and Stripe

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered candy cave and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to Amazon AWS, log in, or create an account and log in. 
* Create a new S3 bucket for the site and create a static directory and media directory within the bucket.
* From the dashboard - copy the bucket details into the settings file.
    * you will require the following:
        - Storage Bucket Name
        - Storage Bucket Region Name
        - Access Key ID
        - Secret Access Key
    * configure these settings in the settings file
* in the env.py file created earlier 
    - add os.environ["AWS_ACCESS_KEY_ID"] = "paste in your access key"
    - add os.environ["AWS_SECRET_ACCESS_KEY"] = "paste in your secret access key"
* In Heroku, add the keys and values copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Using the requirements.txt file install all of the required packages
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.
* This project utilizes Stripe as a payment platform provider - You can create a stripe account at www.stripe.com you will need a developer account to gain access to the api keys required to run the payment processes.
* Once you have successfully created your stripe account, insert the stripe public key, stripe secret key and stripe webhook key into the env.py file and the heroku config vars. Configure the settings file to point at the variables required. Stripe provides documentation on how to setup stripe within django which is easy to follow. It is available within the stripe developer site.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/Olivertrain1221/CandyCave
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

### Credits
* To Code Institute boutique ado for some html and css layout that I found practical for my project are similar just styled differently.
* All images were acquired under license from [Pexels](https://www.pexels.com/) or from [Unsplash](https://unsplash.com/)
* Blog articles based on blog posts on [EKWB](https://www.ekwb.com/)


### Acknowledgements

I'd like to thank the following:
* Tim Nelson for all his help during this project and academic year as my mentor and helping me to hopefully pass this course with this final submission.
* Matt Bodden for all his help with aspects of the project or sometimes just thinking out loud.
* Sean, Ed and Alex at CI Tutor support for their patience and pointing me in the right direction when I went off course.

