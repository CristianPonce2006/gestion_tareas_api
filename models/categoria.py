from sqlmodel import SQLModel, Field

class CategoriaBase(SQLModel):
    nombre: str = Field(nullable=False, max_length=100, min_length=3)

class Categoria(CategoriaBase):
    id: int|None = Field(default=None) 

class CategoriaCreate(CategoriaBase):
    pass
class CategoriaUpdate(CategoriaBase):
    pass