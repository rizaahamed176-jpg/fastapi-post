from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class fast(BaseModel):
    name:str
    age:int
@app.post("/git")
def function(DATA:fast):
    return {"message":DATA.name,"age":DATA.age}