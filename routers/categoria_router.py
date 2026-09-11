from fastapi import APIRouter, HTTPException, status, Query
from models.categoria import Categoria, CategoriaCreate
from sqlmodel import select
from config.session_dependencia import SessionDeDependencia

router = APIRouter()

@router.get("/categorias", response_model=list[Categoria], status_code=status.HTTP_200_OK)
async def get_categorias(session: SessionDeDependencia, offset: int = Query(0, ge=0), limit: int =Query(20, ge=1)):
    consulta = select(Categoria).offset(offset).limit(limit)
    resultado_consulta = session.exec(consulta)
    return resultado_consulta.all()

@router.get("/categorias/{id}", response_model=Categoria, status_code=status.HTTP_200_OK)
async def get_categoria(id: int,session: SessionDeDependencia):
    consulta = select(Categoria).where(Categoria.id == id)
    resultado_consulta = session.exec(consulta)
    if not resultado_consulta:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return resultado_consulta

