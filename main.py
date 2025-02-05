from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(), first_name="Luana", last_name="Channing", gender=Gender.female, roles=[Role.student]),
    User(id=uuid4(), first_name="Alex", last_name="Jones", gender=Gender.male, roles=[Role.admin, Role.user])

]

# First route
@app.get('/')
async def root():
    return {"Hello": "Rich World"}