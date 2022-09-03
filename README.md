# fast-api

# Framework Intro 
- A super fast Python Web Framework 
- Other framework : **Django / Flask / other**
- fast api is very very modern 
- has a very nice feature of a synchronous programming which is still lacking in django framework 

# Fast API Features 
## Automatic Docs
Best thing for the fast API

**1. Swagger UI**
  - genrally we use the postman but thats not a good thing.
  - So by default, fast api provide you the swagger ui where we can simply check what are the routes we have created or api endpoints we have       created. 
  - We can also try them out check what is we are creating , how it is going to respond
  
**2. ReDoc** 
  - having a very nice and minimal design for the documentation

## Just Modern Python
1. Python 3.6 with type using Pydantic library
  - No new syntax to learn. Just standard modern Python.

## Based on Open Standards
1. JSON schema
  - by default returns json which every modern api need to communicate with other things
2. Open API
  - is a linux foundation under linux foundation and it defined how we create our api 
## Editor support 
- vs code : autocomplete feature
- pycharm : autocomplete 

## Security and authentication
- HTTP Basic
- OAuth2 (also with JWT tokens)
- API keys is 
  - Headers
  - Query parameters 
  - Cookies, etc.
## Dependency Injection Unlimited "plug-ins" tested
## Scarlette Features

FastAPI is actually a sub-class of Starlette. So, if you already know or use Starlette, most of the functionality will work the same way.

- WebSocket support 
- GraphQL support
- In-process background tasks
- Startup and shutdown events
- Test client built on requests
- CORS, GZip, Static Files, Streaming responses
- Session and Cookie support 

## Other Supports 
- SQL databases
- NOSQL databases
- GraphQL

## Getting Started
- Install and Setup
- Break it down, how it structured
## Basic Concepts 
- Path Prameters
- API Docs - swagger / redocs
- Query Pramaeters
- Request body 
## Intermediate Concept 
- Debugging FastAPI
- Pydantic Schemas
- SqlAlchemy database connection
- Models and table
## Database Tasks
- Store blog to database 
- Get blogs from database 
- Delete
- Update
## Responses
- Handling Exception
- Return response
- Define response model
## User and Password
- Create User
- Hash User Password
- Show single user
- Define docs tags 
## Relationship
- Define User to Blog Relationship
- Define Blog to user Relationship
## Refactoring for Bigger Application
- API Router
- API Router with parameters
# Authentication using JWT 
JWT - Json Web Token
- Create Login route 
- Login and verify password 
- Return JWT access token
- Routes behind authentication
# Deploy FastAPI
- using Deta.sh website to deploy 
# Final Product 
![image](https://user-images.githubusercontent.com/37190335/187860097-44a3c856-45d2-461c-bb5f-bfb12f90acff.png)
We can also see the same thing with redocs

# fast api Github
https://github.com/tiangolo/fastapi

# Language 
Python 3.6+ version 
# Install and Set Up 

fastapi: The framework on which we’ll build our application.
uvicorn: An Asynchronous Server Gateway Interface module to run our application.

1. Install Python 3.6 or greater version
2. Install fast api
Overall install or for venv 
```
pip install fastapi
```
or 
```
pip3 install fastapi
```
4. Install Uvicorn
```
pip install uvicorn
```
or 
```
pip3 install uvicorn
```
check version
```
uvicorn --version
```
3. Code
```main.py```
```
from typing import Union

from fastapi import FastAPI
# Creating new instance of FASTAPI
app = FastAPI() 
@app.get("/")
def index():
    return 'heyy'
```

4. Execute on terminal to run Server

```
uvicorn main:app --reload
```
## From Book
# Docker 

# Building a simple FastAPI application (ch 1)
We have see how we can run a little demo of app with fast api app.
Now we will explain the steps in here.

- Activate virtual environment
   ```
   env/Scripts/activate
   ```
- We will create a new instance of FastAPI as follows.By instantiating FastAPI in the app variable, we can proceed to create routes

  In app.py or main.py add
    ```
      from fastapi import FastAPI
      app = FastAPI()
    ``` 

- A route is created by first defining a decorator to indicate the type of operation, followed by a function containing the operation to be carried out when this route is invoked.

  In the following example, we’ll create a "/" route that only accepts GET requests and returns a welcome message when visited:

  ```
  @app.get("/")
  async def welcome() -> dict:
      return { "message": "Hello World"}
    ```
-  The next step is to start our application using uvicorn. In your terminal, run the following command:
  
    ```
    uvicorn main:app --reload
    ``` 
   In the preceding command, uvicorn takes the following arguments:
   
   - file:instance: The file containing the instance of FastAPI and the name variable holding the FastAPI instance.
   - --port PORT: The port the application will be served on.
   - --reload: An optional argument included to restart the application on every file change.
      
-   The response from the application logged in your console will be the following:

    ```    {"message":"Hello World"}```

# Routing in Fast API 

- Routing is an essential part of building a web application. In fast api, it is flexible and hassle free.
- Routing in fast API is flexible and hassle free
- It is the process of **handling HTTP requests** **sent from a client to the server**
- HTTP requests are sent to defined routes, which have defined handlers for processing the requests and responding. These handlers are called **route handlers**.

  **Note: An HTTP request is made by a client, to a named host, which is located on a server. The aim of the request is to access a resource on the server. To make the request, the client uses components of a URL (Uniform Resource Locator), which includes the information needed to access the resource.**

  By the end of this chapter, we will know how to create routes using the APIRouter instance and connect to the main FastAPI application.

  Also will learn what path and query parameters are and how to use them in our FastAPI application

  The knowledge of routing in FastAPI is essential in building small- and large-scale applications.

  In this chapter , we will be covering :

  - Routing in FastAPI
  - The APIRouter class
  - Validation using Pydantic models
  - Path and query parameters
  - Request body
  - Building a simple CRUD app
# Understanding routing in FastAPI

- A route is defined to accept requests from an HTTP request method and optionally take parameters
- When a request is sent to a route, the application checks whether the route is defined before processing the request in the route handler.
- On the other hand, a route handler is a function that processes the request sent to the server

An example of a route handler is a function that retrieves records from a database when a request is sent to a router via a route.

# WHAT ARE HTTP REQUEST METHODS?

- HTTP methods are identifiers for indicating the type of action to be carried out
- The standard methods include GET, POST, PUT, PATCH, and DELETE. You can learn more about HTTP methods below :

**GET**
- The GET method requests a representation of the specified resource. 
- Requests using GET should only retrieve data.

**HEAD**
- The HEAD method asks for a response identical to a GET request, but without the response body.

**POST**
- The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

**PUT**
- The PUT method replaces all current representations of the target resource with the request payload.

**DELETE**
- The DELETE method deletes the specified resource.

**CONNECT**
- The CONNECT method establishes a tunnel to the server identified by the target resource.

**OPTIONS**
- The OPTIONS method describes the communication options for the target resource.

**TRACE**
- The TRACE method performs a message loop-back test along the path to the target resource.

**PATCH**
- The PATCH method applies partial modifications to a resource.
# Routing example

- create todo.py

```main.py```

```
from typing import Union

from fastapi import FastAPI
from todo import todo_router
# Creating new instance of FASTAPI
 
app = FastAPI()
 

@app.get("/")
async def say_hello() -> dict:
    return {"message": "Hello!"}
app.include_router(todo_router)
```
```todo.py```

```
from typing import Union

from fastapi import FastAPI, APIRouter
# Creating new instance of FASTAPI
 
 
todo_router=APIRouter()
todo_list = []
@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
```
Then execute :

```
(venv) uvicorn main:app --reload
```









