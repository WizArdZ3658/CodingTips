# Coding Tips
A website where programmers can share their projects, hacks and some cool programming tips. 
Click [here](https://codingtips.herokuapp.com/) to access the website.

## Features :-
 * Users can register, setup their profile (used AWS S3 bucket for storing profile pictures), login/logout etc..
 * Users have to activate their accounts by clicking on the activation link sent to the user's e-mail ID.
 * Users can recover password if they forget.
 * Users can post, write comments, like posts.
 * Users can use markdown or may use tools from top panel to make blog look more beautiful and presentable 
 (similar to StackOverflow) along with real time preview of the content.
 * View posts made by a specific user. 
 * Upvote/Downvote system in comments section, implemented using AJAX.
 * Implemented pagination for better readability.
 * The website also features a search box where users can search for a specific post.
 * Implemented REST API where everyone can see the users details (username, name, DOB, country of origin, profile 
 link). 

## Working with the API
access the link here : https://codingtips.herokuapp.com/api/profiles/

## Technology Stack
##### Languages :-
Python, HTML, CSS, SQL, Javascript

##### Frameworks, Libraries and Tools:-
AJAX, Bootstrap, Django, Heroku-CLI, AWS(S3-bucket), PyCharm, JWT, Django REST framework, Django Crispy Forms, 
Django Pagedown, Django Markdown Deux, JQuery, Marked.js, Django Countries, Django dob Widget, Git

##### Databases:-
SQLite(for development), Postgresql(for production)

##### Environment:-
Windows(my PC), Linux(Deployment server)
