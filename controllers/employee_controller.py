from fastapi import APIRouter, Depends, HTTPException
from services.employee_service import *
from databases.repository import get_db
from schemas.employee_schema import Employee

employee = APIRouter()

@employee.get('/employee', response_model=list[Employee])
async def get_all(db:Session = Depends(get_db)):
    return get_employees(db)

@employee.get('/employee/{employee_id}', response_model=Employee)
async def get_one(employee_id:int , db:Session = Depends(get_db)):
    employee = get_employee(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    return employee

@employee.get('/employee/{employee_identity_number}/identity_number', response_model=Employee)
async def get_one_by_identity_number(employee_indentity_number:str , db:Session = Depends(get_db)):
    employee = get_employee_by_identity_number(db, employee_indentity_number)
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found")
    return employee

@employee.get('/employee/{employee_firstname}/firstname', response_model=list[Employee])
async def get_one_by_firstname(employee_firstname:str , db:Session = Depends(get_db)):
    employee = get_employee_by_firstname(db, employee_firstname)
    if employee is None:
        raise HTTPException(status_code=404, detail="Not found")
    return employee

@employee.post('/employee', response_model=Employee)
async def insert_one(employee:EmployeeCreate, db:Session = Depends(get_db)):
    return insert_employee(db, employee)

@employee.put('/employee/{employee_id}', response_model=Employee)
async def update_one(employee_id:int, employee:EmployeeUpdate, db:Session = Depends(get_db)):
    return update_employee(db, employee_id, employee)

@employee.put('/employee/{employee_id}/is_finish', response_model=Employee)
async def update_one_is_finish(employee_id:int, employee:EmployeeFinish, db:Session = Depends(get_db)):
    return update_employee_is_finish(db, employee_id, employee)

@employee.delete('/employee/{employee_id}')
async def delete_one(employee_id:int, db:Session = Depends(get_db)):
    return delete_employee(db, employee_id)