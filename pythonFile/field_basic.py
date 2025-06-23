from pydantic import BaseModel, Field
from typing import List, Dict, Optional

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)
class Employee(BaseModel):
    id : int
    name : str = Field(
        ..., # Required 
        min_length=3,
        max_length=50,
        description='Emplyoee name',
        examples='Manav Desai',
        default=None
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ...,
        gt = 10000, #ge(greater equal),
    )