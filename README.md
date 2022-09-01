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

app = FastAPI()
@app.get("/")
def index():
    return 'heyy'
```
5. 





