from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    zip_code : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    created_at : datetime
    address : Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={ datetime : lambda v: v.strftime('%d-%m-%Y %H:%M:%S') }
    )
# create a user instance
user = User(
    id=1,
    name='Manav',
    email='abc@gmail.com',
    created_at=datetime(year=2024, month=6, day=4, hour=3, minute=43),
    address= Address(
        street = 'abcd',
        city='surat',
        zip_code = 'nvfd'
    ),
    tags=['python', 'Javascript']
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(type(python_dict))
print(python_dict)
print('==='*50)

# Using model_dump_json() -> json
json_str = user.model_dump_json()
print(type(json_str))
print(json_str)