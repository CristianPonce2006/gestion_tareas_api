import sqlmodel import SQLModel, Field
from typing import Optional

class CategoriaBase(SQLModel):
    nombre: str = Field(nullable=False, max_length=100, min_length=3)
    
class CategoriaCreate(CategoriaBase):
    pass
class CategoriaUpdate(CategoriaBase):
    pass