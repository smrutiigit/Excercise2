from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Column, Float, String, Integer

app = FastAPI()

#SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./emp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
#engine = create_engine("sqlite:///./emp.db", pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# A SQLAlchemny ORM Place
class DBItem(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    employee_id= Column(String)
    city = Column(String, nullable=True)
    experience = Column(Float)
    ctc = Column(Float)
    age = Column(Float)
    contact= Column(String)
Base.metadata.create_all(bind=engine)


#Pydantic place
class Item(BaseModel):
    first_name: str
    last_name:str
    employee_id: str
    city: str
    experience: float
    ctc:float
    age:float
    contact: str
class Config:
    orm_mode = True

# Methods for interacting with the database
def get_item(db: Session, item_id: int):
    return db.query(DBItem).where(DBItem.id == item_id).first()

def get_items(db: Session):
    return db.query(DBItem).all()

def create_item(db: Session, item: Item):
    db_item = DBItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Routes for interacting with the API
@app.post('/items/', response_model=Item)
def create_items_view(place: Item, db: Session = Depends(get_db)):
    db_item = create_item(db, place)
    return db_item

@app.get('/items/', response_model=List[Item])
def get_places_view(db: Session = Depends(get_db)):
    return get_items(db)

@app.get('/item/{item_id}')
def get_item_view(item_id: int, db: Session = Depends(get_db)):
    return get_item(db, item_id)

@app.get('/')
async def root():
    return {'message': 'Hello World!'}


#@app.post("/items/")
#def create_item(item:Item):
#   return item


