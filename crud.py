from sqlalchemy.orm import Session
import model
import schema


def get_emp_by_employee_id(db: Session, employee_id: str):
     return db.query(model.Emps).filter(model.Emps.employee_id == employee_id).first()


def get_emp_by_id(db: Session, sl_id: int):
    return db.query(model.Emps).filter(model.Emps.id == sl_id).first()


def get_emp(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all employee details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.Emps).offset(skip).limit(limit).all()


def add_emp_details_to_db(db: Session, emp: schema.EmpAdd):
    
    emp_details = model.Emps(
        employee_id=emp.employee_id,
        first_name=emp.first_name,
        last_name=emp.last_name,
        city=emp.city,
        experience=emp.experience,
        age=emp.age,
        contact=emp.contact
    )
    db.add(emp_details)
    db.commit()
    db.refresh(emp_details)
    return model.Emps(**emp.dict())


#def update_emp_details(db: Session, sl_id: int, details: schema.UpdateEmp):
#    db.query(model.Emps).filter(model.Emps.id == sl_id).update(vars(details))
#    db.commit()
#    return db.query(model.Emps).filter(model.Emps.id == sl_id).first()


#def delete_emp_details_by_id(db: Session, sl_id: int):
#    try:
#        db.query(model.Emps).filter(model.Emps.id == sl_id).delete()
#        db.commit()
#    except Exception as e:
#        raise Exception(e)