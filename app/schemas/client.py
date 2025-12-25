from pydantic import BaseModel, EmailStr

class ClientCreate(BaseModel):
    name: str
    email: EmailStr

class ClientRead(BaseModel):
    id: int
    name: str
    email: EmailStr
