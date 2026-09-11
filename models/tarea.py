from sqlmodel import SQLModel, Field
from typing import Optional

class TareaBase(SQLModel):
    usuario_id:int = Field(nullable=False, foreign_key="usuarios.id")
    categoria_id: int = Field(nullable=False, foreign_key="categorias.id")
    titulo: str = Field(nullable=False, max_length=200, min_length=3)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    completada: bool = Field(default=False)

class Tarea(TareaBase, table=True):
    __tablename__ = "tareas" #type: ignore
    id: int|None = Field(default=None, primary_key=True) 

class TareaCreate(TareaBase):
    pass
class TareaUpdate(TareaBase):
    pass