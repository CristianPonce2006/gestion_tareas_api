from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.db import crear_db_y_tablas
from routers.categoria_router import router as categorias_router
from routers.tareas_router import router as tareas_router
from routers.usuario_router import router as usuarios_router
import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_db_y_tablas()
    yield

app = FastAPI(lifespan=lifespan)
app.title = "API Tienda X"
app.version = "0.0.1"
origins = [
    "http://localhost",
    "http://localhost:9000", # Cambia esto por el puerto exacto de tu app Flutter
    # "*", # Puedes usar un asterisco en desarrollo para permitir cualquier origen
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permite todos los headers
)
@app.get("/", summary="Comprobando Api", status_code=status.HTTP_200_OK)
async def home():
    return {"message": "ok"}

app.include_router(categorias_router, tags=["categorias"])
app.include_router(tareas_router, tags=["tareas"])
app.include_router(usuarios_router, tags=["usuarios"])