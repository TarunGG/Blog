
# Blog Manager


## Overview
It is an API developed in python that allows you to create a blog with a title, description and your username. It is very simple to use and you can use it to create your own blog.

### Getting Started:
 To get started just copy this link <https://blog-api-1.herokuapp.com/> and paste it in postman or thunder client and you are good to go. Send a **GET** request to the link to get all available endpoints of the API.



### API Endpoints:

1. ***all/*** :-
Send a **GET** request to this endpoint to get all the blogs in the database.The format of the response will be:

***Response*** :-
{
  "posts": [
    {
      "id": 1,
      "title": "My first blog",
      "description": "This is my first blog",
      "username": "John"
      "created at": "2021-08-31"
      "last updated": "2021-08-31"
    },
    {
      "id": 2,
      "title": "My second blog",
      "description": "This is my second blog",
      "username": "John"
    }
  ]
}

In above request if any error occurs then it will return an error message in the response with success = false.


2. ***all/\<id\>/*** :-
Send a **GET** request to this endpoint to get a specific blog with the provided id from the database.The format of the response will be:

***Request*** :-
Method: **GET**
https://blog-api-1.herokuapp.com/all/1

***Response*** :-
{
  "post": {
    "id": 1,
    "title": "My first blog",
    "description": "This is my first blog",
    "username": "John"
  }
}

In above request if any error occurs then it will return an error message in the response with success = false.


3. ***create/*** :-

Send a **POST** request to this endpoint to create a new blog(s) in the database.The format of the request will be:

***Request*** :-
https://blog-api-1.herokuapp.com/create/
METHOD : **POST**
{
  "posts": [
    {
      "title": "My first blog",
      "description": "This is my first blog",
      "usename": "John"
    }
    ]
}

In above request you can create as many blogs as you want by adding them in the blogs array. Here "title" and "description" are required fields where as "username" field is optional.
In above request if any error occurs then it will return an error message in the response with success = false.

***Response*** :-
{
  "success": "true",
  "posts": [
    {
      "id": <id of the blog>,
      "title": "My first blog",
      "status": "Post created"
    }
  ]
}


4. ***create/<id>/*** :-
 Send a PUT request to this endpoint to update a specific blog with the provided id from the database.The format of the request will be:

***Request*** :-
Method: PUT
https://blog-api-1.herokuapp.com/create/1

{
  "title": "New title",
  "description": "New description",
  "usename": "New username"
}

In above request you have to provide atleast one field to update the blog.If you provide even one of any of the three fields then the request will be processed otherwise it will return an error. Here you can't update the id of the blog.

***Response*** :-
{
  "success": "true",
  "response": "Post updated successfully"
}



5. ***delete/<id>/*** :-
Send a **DELETE** request to this endpoint to delete a specific blog with the provided id from the database.The format of the response will be:

***Response*** :-
{
  "success": "true",
  "response": "Post with id=<id> successfully deleted."
}