from pydantic import BaseModel

class EmpBase(BaseModel):
    employee_id: int
    first_name: str
    last_name:str
    city: str
    experience: float
    ctc:float
    age:float
    contact: str

class EmpAdd(EmpBase):
    employee_id: str
    
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class Emp(EmpAdd):
    id: int
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateEmp(BaseModel):
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True
