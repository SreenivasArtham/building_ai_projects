from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator


class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, frozen=True)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0)
    is_active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v <= 0:
            raise ValueError("Age must be a positive integer")
        return v    

# Test with clean data
def test_user_model():
    print("Testing User model with valid data...")
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30,
        "is_active": True,
        "created_at": datetime.now(),
    }
    user = User(**user_data)
    print(user)


# Test with invalid email
def test_invalid_email():
    print("\nTesting User model with invalid email...")
    user_data = {
        "name": "Jane Doe",
        "email": "jane.doe@invalid-email",
        "age": 25,
        "is_active": True,
        "created_at": datetime.now(),
    }
    try:
        user = User(**user_data)
    except ValidationError as e:
        print(f"Validation error:\n{e}")

def test_missing_fields():
    print("\nTesting User model with missing fields...")
    user_data = {
        "name": "Alice",
        "age": 28,
    }
    try:
        user = User(**user_data)
    except ValidationError as e:
        print(f"Validation error:\n{e}")

def test_serialization():
    print("\nTesting User model serialization...")
    user_data = {
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "age": 35,
        "is_active": False,
        "created_at": datetime.now(),
    }
    user = User(**user_data)
    print(user.model_dump_json(indent=4))  # Serialize to JSON with indentation
    
    print(user.model_dump())  # Serialize to dictionary

def test_field_constraints():
    print("\nTesting User model with field constraints...")
    user_data = {
        "name": "",  # Invalid: empty name
        "email": "invalid-email",  # Invalid email
        "age": -5,  # Invalid: negative age
        "is_active": True,
        "created_at": datetime.now(),
    }
    try:
        user = User(**user_data)
    except ValidationError as e:
        print(f"Validation error:\n{e}")    

def test_field_custom_validators():
    print("\nTesting User model with custom validators...")
    user_data = {
        "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "age": 0,
        "is_active": True,
        "created_at": datetime.now(),
    }
    try:
        user = User(**user_data)
        print(user)
    except ValidationError as e:
        print(f"Validation error:\n{e}")

if __name__ == "__main__":
    test_user_model()
    test_invalid_email()
    test_missing_fields()
    test_serialization()
    test_field_constraints()
    test_field_custom_validators()
