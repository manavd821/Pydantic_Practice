from flask import Flask
from pydantic import BaseModel, EmailStr
app = Flask(__name__)

class SignUp(BaseModel):
    username : str
    email : EmailStr
    password : str

class Settings(BaseModel):
    app_name : str = 'Myapp'
    admin : str = 'admin@gmail.com'

def get_settings():
    return Settings()

@app.post('/signup')
def signup(user : SignUp):
    return {'message' : f'User {user.username} signed up'}

@app.get('/settings')
def get_settings_endpoint(settings : Settings):
    return settings
