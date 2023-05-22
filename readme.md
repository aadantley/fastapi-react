# FastAPI and React

## Description

A project with an API written in python's FastAPI library, and a frontend written in React.

Based on the playlist: <https://www.youtube.com/playlist?list=PLU7aW4OZeUzwYXbC_mbQJdAU7JUu81RZo>

## Tutorial Notes

### Pydantic Models and Tortoise ORM

Uses Pydantic models using tortoise ORM for the database design (video 1).

Steps:

- create a virtual environment.
- pip install `fastapi`, `uvicorn` and `tortoise-orm` libraries.
- the command to start the app is `uvicorn app:app`. This is the name of the file followed by what the FastAPI instance is named in your file.

## Take Aways

### Video 1

#### FastAPI setup

- setting up a fastAPI file is very similar to setting up a flask file
- FastAPI runs on port `8000` like Django.
- FastAPI takes care of JSONifying the output data.
- FastAPI with uvicorn automatically adds a swagger documentation page at the endpoint.
- **NOTE**: needed to reference fastAPI documentation for update on how to handle decorator for fastAPI endpoints. but this, along with adding `--reload` to the command to run the fastapi server helped to get the `hello world` endpoint up and running. I removed the `async` keyword from the fastAPI quick start though.

#### Models Development

- We use the Tortoise API to create Model classes, very similar to Django. The models are created in a `models.py` file.
- Then we create pydantic models; this is similar to creating serializers in Django. You can create these to accept user input for the fields that are not read-only.
- Then we need to create a database to interact with, using the tortoise API.
  - **NOTE**: when defining foreign keys in your models in tortoise ORM, you have to capitalize the class name you are referencing. So I got an error because I had `models.supplier` instead of `models.Supplier`.

## To Dos

- continue with video 3: CRUD API functionality.
