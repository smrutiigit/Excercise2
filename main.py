from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    first_name: str
    last_name:str
    employee_id: str
    city: str
    experience: float
    ctc:float
    age:float
    contact: str

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item:Item):
   return item

