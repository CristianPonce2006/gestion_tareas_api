from fastapi import APIRouter, HTTPException, status, Query
from models.tarea import Tarea, TareaCreate
from models.usuario import Usuario
from models.categoria import Categoria
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

@router.post("/tareas", response_model=Tarea, status_code=status.HTTP_201_CREATED)
async def create_tarea(session: SessionDeDependencia, data: TareaCreate):
    #validamos si existe la categoría
    consulta_categoria = select(Categoria).where(
        Categoria.id == data.categoria_id
    )
    categoria = session.exec(consulta_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail=f"Categoría con id: {data.categoria_id} no encontrada")
    
    #validamos si existe el usuario
    consulta_usuario = select(Usuario).where(
    Usuario.id == data.usuario_id
    )
    usuario = session.exec(consulta_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail=f"Usuario no encontrado")
    
    tarea_nueva = Tarea(
        usuario_id=data.usuario_id,
        categoria_id=data.categoria_id,
        titulo=data.titulo,
        descripcion=data.descripcion
    )
    try:
        session.add(tarea_nueva)
        session.commit()
        session.refresh(tarea_nueva)
        return tarea_nueva
    except:
        raise HTTPException(status_code=500, detail="Error al guardar tarea")