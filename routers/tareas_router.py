from fastapi import APIRouter, HTTPException, status, Query
from models.tarea import Tarea, TareaCreate
from sqlmodel import select
from config.session_dependencia import SessionDeDependencia

router = APIRouter()

@router.get("/tareas", response_model=list[Tarea], status_code=status.HTTP_200_OK)
async def get_tareas(session: SessionDeDependencia, offset: int = Query(0, ge=0), limit: int =Query(20, ge=1)):
    consulta = select(Tarea).offset(offset).limit(limit)
    resultado_consulta = session.exec(consulta)
    return resultado_consulta.all()

@router.get("/tareas/{id}", response_model=Tarea, status_code=status.HTTP_200_OK)
async def get_tarea(id: int,session: SessionDeDependencia):
    consulta = select(Tarea).where(Tarea.id == id)
    resultado_consulta = session.exec(consulta).first()
    if not resultado_consulta:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return resultado_consulta

