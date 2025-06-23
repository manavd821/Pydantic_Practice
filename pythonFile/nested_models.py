from pydantic import BaseModel #type: ignore
from typing import List, Optional

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    address : Address

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(
    street='123 something',
    city= 'Surat',
    postal_code='1001'
)
user = User(
    id=1,
    name='Manav',
    address= address
)

comment = Comment(
    id = 1,
    content = 'Hare Krsna',
    replies= [
        Comment(id=2, content='reply1' ),
        Comment(id=3, content='reply2' ),
    ]
)
# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Lession(BaseModel):
    lession_id : int
    topic : str

class Module(BaseModel):
    module_id : int
    name : str
    lessions : List[Lession]
    
class Course(BaseModel):
    course_id : int
    title : str
    modules : List[Module]