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
- [Docker](https://docs.docker.com/get-docker/) and docker-compose installed
- Docker engine running
- [Git](https://git-scm.com/downloads) installed (for cloning the repository)

## Installation

1. Clone the repository
   ```
   git clone 
   ```
2. Go to the project directory
3. Create a python virtual enviroment (venv):
   ```
   python -m venv env
   ```
4. Activate the enviroment using the scripts at:   `.\env\Scripts`
   
   For example on Windows cmd:
   ```
   .\env\Scripts\activate.bat
   ```
5. Create the container with the database:
   ```
   docker-compose --build -d
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
Remarks:The CPF must be a valid one.

### Get a list of all users

Send a GET request to `/users`.

### Get details of a specific user

Send a GET request to `/users/<user_id>`.

### Update a user

Send a PUT request to `/users/<user_id>` with the following data:

```json
{
    "name": "New User Name",
    "cpf": "New User CPF",
    "age": "New User Age"
}
```

### Delete a user

Send a DELETE request to `/users/<user_id>`.

## License

This project is licensed under the terms of the MIT license.