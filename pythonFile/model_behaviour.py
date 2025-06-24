from pydantic import BaseModel, field_validator, model_validator, computed_field, Field

class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls, value):
        if len(value) < 3:
            raise ValueError('Username must be atleast four characters')
        else: return value

class SignUp(BaseModel):
    password : str
    confirm_password : str

    @model_validator(mode='after')
    def password_match(cls, value):
        if value.password != value.confirm_password:
            raise ValueError("Password don't match")
        else: return value

class Product(BaseModel):
    price : float
    quantity : int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(..., ge=1)
    rate_per_night : float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


