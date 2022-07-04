from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Employee Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

@app.get('/retrieve_all_emps_details', response_model=List[schema.Emp])
def retrieve_all_emps_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    emps = crud.get_emps(db=db, skip=skip, limit=limit)
    return emps


@app.post('/add_new_emp', response_model=schema.EmpAdd)
def add_new_emp(emp: schema.EmpAdd, db: Session = Depends(get_db)):
    employee_id = crud.get_emp_by_employee_id(db=db, employee_id=emp.employee_id)
    if employee_id:
        raise HTTPException(status_code=400, detail=f"Employee id {emp.employee_id} already exist in database: {employee_id}")
    return crud.add_emp_details_to_db(db=db, emp=emp)


#@app.delete('/delete_emp_by_id')
#def delete_emp_by_id(sl_id: int, db: Session = Depends(get_db)):
#   details = crud.get_emp_by_id(db=db, sl_id=sl_id)
 #   if not details:
  #      raise HTTPException(status_code=404, detail=f"No record found to delete")

   # try:
    #    crud.delete_emp_details_by_id(db=db, sl_id=sl_id)
    #except Exception as e:
    #    raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    #return {"delete status": "success"}


#@app.put('/update_emp_details', response_model=schema.Emp)
#def update_emp_details(sl_id: int, update_param: schema.UpdateEmp, db: Session = Depends(get_db)):
#    details = crud.get_emp_by_id(db=db, sl_id=sl_id)
#    if not details:
#       raise HTTPException(status_code=404, detail=f"No record found to update")
#
#    return crud.update_emp_details(db=db, details=update_param, sl_id=sl_id)
    


