from fastapi import APIRouter, HTTPException, status, Query
from models.usuario import Usuario, UsuarioCreate
from sqlmodel import select
from config.session_dependencia import SessionDeDependencia

router = APIRouter()

@router.get("/usuarios", response_model=list[Usuario], status_code=status.HTTP_200_OK)
async def get_Usuarios(session: SessionDeDependencia, offset: int = Query(0, ge=0), limit: int =Query(20, ge=1)):
    consulta = select(Usuario).offset(offset).limit(limit)
    resultado_consulta = session.exec(consulta)
    return resultado_consulta.all()

@router.get("/usuarios/{id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def get_Usuario(id: int,session: SessionDeDependencia):
    consulta = select(Usuario).where(Usuario.id == id)
    resultado_consulta = session.exec(consulta).first()
    if not resultado_consulta:
        raise HTTPException(status_code=404, detail="Usuario no encontrada")
    return resultado_consulta

