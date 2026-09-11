from sqlmodel import SQLModel, Field
from pydantic import EmailStr
class UsuarioBase(SQLModel):
    nombre: str = Field(nullable=False, max_length=100, min_length=3)
    email: str = Field(nullable=False, max_length=150, min_length=3)
class Usuario(UsuarioBase, table=True):
    __tablename__ = "usuarios" #type: ignore
    id: int|None = Field(default=None, primary_key=True) 

class UsuarioCreate(UsuarioBase):
    pass
class UsuarioUpdate(UsuarioBase):
    pass