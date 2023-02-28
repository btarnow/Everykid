# Everykid 
Discover children’s books with diverse characters 📚

There is a disparity around who is represented in children’s books, so Everykid exists to help people find children’s books that celebrate diversity. Users can discover books by the racial and/or gender identity of the main character and add books to their collection. The goal is for every kid to see themselves represented in a book.

**Demo Site:** http://18.216.150.110/

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
* Planning: DB Designer & Figma 
* Data Model: 
![Data Model](/static/screenshots/data_model.png)

## Features
🎥 [See a full video walk-through](https://youtu.be/d1moGgvH0Ew)

### Homepage
* Users start at an empty state/basic landing page where they can filter books by a main character’s racial and/or gender identity
![Homepage](/static/screenshots/homepage.png)

### Book Results Page
* The user is taken to a book results page where they are shown books that meet their criteria 
* I utilized SQLAlchemy to optimize database queries to display relevant books 
![Book Results Page](/static/screenshots/book-results.png)

### Login 
* Users can create an account to save books they are interested in
* To protect the user’s password, I used a ​​cryptographic hashing algorithm that stores a hashed version of the user’s password to my database
![Book Results Page](/static/screenshots/login.png)

### Book Details Page 
* The user can view individual book details and save the book to their personal collection
* This page includes a "Books You May Like" section to help users discover more books that characters with similar identities
![Book Details Page](/static/screenshots/book-details.png)

### User's Profile Page
* Users can access their personally curated book collection by going to the ‘My Books’ portion of their profile

## Future Improvements
* Allow users to add and delete books from their My Books collection from multiple avenues 
* Utilize AJAX on the homepage to show book results from the user's input without routing to a different page

## Set Up
To run this project locally, first clone or fork this repo:
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

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/becky-tarnowski/)!




