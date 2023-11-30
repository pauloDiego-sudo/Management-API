# User Management API

This project is a simple User Management API built with Flask, SQLAlchemy, and Marshmallow.

## Features

- Create a new user
- Get a list of all users
- Get details of a specific user
- Update a user
- Delete a user

## Pre-Requirements
Before running the project, make sure you have the following:

- [Python](https://www.python.org/downloads/) installed on your system
   - Specially with python3.11 [venv](https://docs.python.org/3/library/venv.html) 
- [Docker](https://docs.docker.com/get-docker/) and docker-compose installed
- Docker engine running
- [Git](https://git-scm.com/downloads) installed (for cloning the repository)

## Installation

1. Clone the repository
   ```
   git clone git@github.com:pauloDiego-sudo/Management-API.git
   ```
2. Go to the project directory
3. Create a python virtual enviroment (venv):
   ```
   python -m venv env
   ```
4. Activate the enviroment using the scripts:   
   For example on Windows cmd:
   ```
   .\env\Scripts\activate.bat
   ```
   For Linux
   ```
   source \env\bin\activate
   ```
5. Create the container with the database:
   For Windows:
   ```
   docker-compose --build -d
   ```
   For Linux:
   ```
   docker-compose up
   ```
   Make sure the docker engine is running.
  
6. Install the dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
7. Run the server:
   ```
   python api.py
   ```

## Usage

### Create a new user

Send a POST request to `/users` with the following data:

```json
{
    "name": "User Name",
    "cpf": "User CPF",
    "age": "User Age"
}
```
Remarks:The CPF must be a valid one. You can use tools like [Gerador De CPF](https://www.geradordecpf.org) to generate a valid one.

For example, using cURL:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "UserName", "cpf": "651.433.647-79", "age": "30"}' http://localhost:5000/users
```

### Get a list of all users

Send a GET request to `/users`.

For example, using cURL:
```
curl -X GET http://localhost:5000/users
```

### Get details of a specific user

Send a GET request to `/users/<user_id>`.

For example, using cURL:
```
curl -X GET http://localhost:5000/users/<user_id>
```
OBS: You must replace `<user_id>` with a valid (and existing) id.

### Update a user

Send a PUT request to `/users/<user_id>` with the following data:

```json
{
    "name": "New User Name",
    "cpf": "New User CPF",
    "age": "New User Age"
}
```
For example, using cURL:
```
curl -X PUT -H "Content-Type: application/json" -d '{"name": "UserName", "cpf": "651.433.647-79", "age": "30"}' http://localhost:5000/users/<user_id>
```

### Delete a user

Send a DELETE request to `/users/<user_id>`.

For example, using cURL:
```
curl -X DELETE http://localhost:5000/users/<user_id>
```
OBS: You must replace `<user_id>` with a valid (and existing) id.

## License

This project is licensed under the terms of the MIT license.