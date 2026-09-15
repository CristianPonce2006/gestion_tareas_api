from fastapi import APIRouter, HTTPException, status, Query
from models.usuario import Usuario, UsuarioCreate
from sqlmodel import select
from config.session_dependencia import SessionDeDependencia

router = APIRouter()

@router.get("/usuarios", response_model=list[Usuario], status_code=status.HTTP_200_OK)
async def get_usuarios(session: SessionDeDependencia, offset: int = Query(0, ge=0), limit: int =Query(20, ge=1)):
    consulta = select(Usuario).offset(offset).limit(limit)
    resultado_consulta = session.exec(consulta)
    return resultado_consulta.all()

@router.get("/usuarios/{id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def get_usuario(id: int,session: SessionDeDependencia):
    consulta = select(Usuario).where(Usuario.id == id)
    resultado_consulta = session.exec(consulta).first()
    if not resultado_consulta:
        raise HTTPException(status_code=404, detail="Usuario no encontrada")
    return resultado_consulta


@router.post("/usuarios", response_model=Usuario, status_code=status.HTTP_201_CREATED)
async def create_usuario(session: SessionDeDependencia, data: UsuarioCreate):
    usuario_nuevo = Usuario(
        nombre=data.nombre,
        email=data.email
    )
    try:
        session.add(usuario_nuevo)
        session.commit()
        session.refresh(usuario_nuevo)
        return usuario_nuevo
    except:
        raise HTTPException(status_code=500, detail="Error al guardar usuario")
