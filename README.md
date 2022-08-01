# Candy Cave

## Introduction

Candy Cave shop is a website built using the framework Django and using languages such as Python, Javascript, HTML and CSS. The site is a fully functioning ECommerce site for a fictional shop called “Candy Cave” The shop is aimed to be a modern take on an old school sweet shop during the “disco earer” the idea is the user can navigate the site and find sweets and get them added to a basket and delivered to there door. With all the niceties of a fully functioning shop.
The users are able to select different measurements of sweets in grams and are then able to also order 2 lots of seperate 100g this is perfect for someone who likes a variation or may even be thinking of doing a gift bag etc etc.

The site also shows reviews left by valid customers which is important for the site to be successful as a ecommerce store.

This is the fifth project for the Code Institute Diploma in Software Development with eCommerce.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, Full CRUD functionality for approved users for Products, Categories, Blog Posts and Categories along with Reviews and Responses.

![Screenshot of homepage]()

[View the live website on Heroku](https://candycave-computers.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
- [candycave Computers](#candycave-computers)
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
2. Clear Pricing [#2]https://github.com/Olivertrain1221/CandyCave/issues/7)
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

