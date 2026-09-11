from sqlmodel import SQLModel, Field

class CategoriaBase(SQLModel):
    nombre: str = Field(nullable=False, max_length=100, min_length=3)

class Categoria(CategoriaBase, table=True):
    __tablename__ = "categorias" #type: ignore
    id: int|None = Field(default=None, primary_key=True) 

class CategoriaCreate(CategoriaBase):
    pass
class CategoriaUpdate(CategoriaBase):
    pass