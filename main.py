from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3", # defining a route to the database
    modules={"models": ["models"]}, # noting that the models are created from the models.py file
    generate_schemas=True,
    add_exception_handlers=True
)