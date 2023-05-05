# Everykid 
Discover children’s books with diverse characters 📚

There is a disparity around who is represented in children’s books, so Everykid exists to help people find children’s books that celebrate diversity. Users can discover books by the racial and/or gender identity of the main character and add books to their collection. The goal is for every kid to see themselves represented in a book.

**Demo Site:** http://18.216.150.110/

## Table of Contents
* 🤖 [Technologies Used](#technologies-used)
* ⭐ [Features](#features)
* 🚀 [Future Improvements](#future-improvements)
* 📖 [Set Up](#set-up)
* 👩🏼‍💻 [About This Project](#about-this-project)

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
* This page includes a "Books You May Like" section to help users discover more books that have characters with similar identities
![Book Details Page](/static/screenshots/book-details.png)

### User's Profile Page
* Users can access their personally curated book collection by going to the ‘My Books’ portion of their profile
![User's Page](/static/screenshots/user-collection.png)

## Future Improvements
* Allow users to add and delete books from their My Books collection from multiple avenues 
* Utilize AJAX on the homepage to show book results from the user's input without routing to a different page
* Expand the user profile page to allow for users to create multiple collections as well as have access to changing their account information 

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

## About This Project
👩🏼‍💻 Hi, all! I am Becky Tarnowski, and I am software engineer with a background in education. This is my capstone project for an intensive software engineering fellowship that I recently completed. 

This project was inspired by my previous students and a research study I led at 
my school on the relationship between students’ sense of belonging and their representation in our school. The inspiration from my students came when they noticed an inequity around who was represented in the books and our classroom.To work towards a more equitable library, we researched books together that highlighted the stories of more diverse characters and wrote a grant to get them for our classroom. I wished a tool like this existed at the time to help us discover books that celebrate diversity.

The research study on the relationship between belonging and representation also inspired this because the findings of the study showed a correlation between who was represented in our school environment and who felt like they belonged. Finding books that represent and celebrate diverse characters was one way our school worked to increase representation, and I want to help others fill their libraries with books that celebrate every kid too! 

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/becky-tarnowski/)!




