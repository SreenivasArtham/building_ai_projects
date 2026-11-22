from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Employee(BaseModel):
    id: Optional[UUID] = None
    name: str
    email: str
    manager: bool = False

employees = []

@app.get("/employees", response_model=List[Employee])
def read_employee():
    return employees

@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    employee.id = uuid4()
    employees.append(employee)
    return employee

@app.get("/employees/{employee_id}", response_model=Employee)
def read_employee_by_id(employee_id: UUID):
    for employee in employees:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: UUID, updated_employee: Employee):
    for index, employee in enumerate(employees):
        if employee.id == employee_id:
            updated_employee.id = employee_id
            employees[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{employee_id}", response_model=Employee)
def delete_employee(employee_id: UUID):
    for idx,employee in enumerate(employees):
        if employee.id == employee_id:
            deleted_employee = employees.pop(idx)
            return deleted_employee
    raise HTTPException(status_code=404, detail="Employee not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)