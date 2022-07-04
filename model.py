from sqlalchemy import Column, Float, String, Integer
from database import Base

class DBEmp(Base):
    __tablename__ = 'emp'
    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    city = Column(String, nullable=True)
    experience = Column(Float)
    ctc = Column(Float)
    age = Column(Float)
    contact= Column(String)
