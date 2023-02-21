# Everykid
Discover children’s books with diverse characters 📚

There is a disparity around who is represented in children’s books, so Everykid exists to help people find children’s books that celebrate diversity. Users can filter books by the racial and/or gender identity of the main character and add books to their collection. The goal is for every kid to see themselves represented in a book.

## Table of Contents
* 🤖 [Technologies](#technologies-used)
* ⭐ [Features](#features)
* 🚀 [Future Improvements](#future-improvements)
* 📖 [Set Up](#set-up)
* 👩🏼‍💻 [About Me](#about-me)

## Technologies Used
* Backend: Python, Flask, SQL, PostgreSQL, SQLAlchemy
* Frontend: Javascript, HTML, CSS, Bootstrap, JSON, Jinja2, AJAX
* APIs: Open Library’s Books and Authors APIs
* Planning: DB Designer, Figma 
* Data Model: 
![Data Model](/static/screenshots/data_model.png)

## Features
* Users start at an empty state/basic landing page where they can select to filter books by a main character’s racial and/or gender identity

* Once they apply filters, they are taken to a book results page where they are shown books that meet that criteria

* They can click into an individual book to find out more about the book as well as receive recommendations for books they may like based on the selected book’s characters

* Users can create an account/log in to gain access to the functionality of saving books to a collection 

## Future Improvements
* This project is still in progress. I am working to add the functionality of users storing books to their collection and will be styling soon.

* Utilize AJAX within the character identity form to reload matching book results without updating the whole page 

* Add the functionality for users to rate and review books 


## Set Up
To run this project, first clone or fork this repo:
```
git clone https://github.com/btarnow/Everykid.git
```
Create and activate a virtual environment inside your directory
```
virtualenv env
source env/bin/activate
```
Install the dependencies:
```
pip install -r requirements.txt
```

Set up the database:
```
python3 seed_database.py
```
Run the app:
```
python3 server.py
```
You can now navigate to 'localhost:5000/' to access the Everykid app!

## About Me
👩🏼‍💻 Hi, all! I am Becky Tarnowski, and I am an educator turned software engineer. I am currently in an intensive software engineering bootcamp and will be seeking a full-time software engineering job in the second quarter of 2023. This is my capstone project for the program.  

During my seven years as an educator, I worked in Indianapolis Public Schools. When the pandemic hit, I realized that I had a knack for solving problems with technology. For example, when faced with the problem of how to get students their work virtually, I taught myself how to use a learning management system and led software training and enablement sessions for teachers and staff. 

Looking forward, I hope to continue to solve problems with technology as an engineer. 

Feel free to connect with me on LinkedIn: https://www.linkedin.com/in/becky-tarnowski/



