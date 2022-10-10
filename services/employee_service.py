from sqlalchemy.orm import Session
from models.employee import Employee
from schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeFinish

def get_employees(db:Session):
    return db.query(Employee).all()

def get_employee(db:Session, employee_id : int):
    return db.query(Employee).filter(Employee.id==employee_id).first()

def get_employee_by_identity_number(db:Session, employee_indentity_number : str):
    return db.query(Employee).filter(Employee.indentity_number==employee_indentity_number).first()

def get_employee_by_firstname(db:Session, employee_firstname : str):
    return db.query(Employee).filter(Employee.firstname==employee_firstname).all()

def insert_employee(db:Session, employee:EmployeeCreate):
    new_employee = Employee(firstname = employee.firstname, lastname = employee.lastname, years_old = employee.years_old, birthday = employee.birthday, indentity_number = employee.indentity_number, address = employee.address, email = employee.email, start_date = employee.start_date, departure_date = employee.departure_date, user_id = employee.user_id)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee(db:Session, employee_id:int, employee:EmployeeUpdate):
    edit_employee = db.query(Employee).get(employee_id)
    edit_employee.firstname = employee.firstname
    edit_employee.lastname = employee.lastname
    edit_employee.years_old = employee.years_old
    edit_employee.birthday = employee.birthday
    edit_employee.indentity_number = employee.indentity_number
    edit_employee.address = employee.address
    edit_employee.email = employee.email
    edit_employee.start_date = employee.start_date
    edit_employee.departure_date = employee.departure_date
    edit_employee.user_id = employee.user_id
    edit_employee.update_at = employee.update_at
    db.commit()
    return edit_employee

def update_employee_is_finish(db:Session, employee_id:int, employee:EmployeeFinish):
    edit_employee           = db.query(Employee).get(employee_id)
    edit_employee.is_active = employee.is_active
    edit_employee.departure_date = employee.departure_date
    edit_employee.finish_at = employee.finish_at
    db.commit()
    return edit_employee

def delete_employee(db:Session, employee_id:int):
    employee = db.query(Employee).get(employee_id)
    db.delete(employee)
    db.commit()
    return "delete"