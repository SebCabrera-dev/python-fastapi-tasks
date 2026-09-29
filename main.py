from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuracion base de datos
DATABASE_URL = "sqlite:///./tareas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TareaDB(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    completada = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# PYDANTIC schemas
class TareaCreate(BaseModel):
    titulo: str
    descripcion: str
    completada: bool = False

class TareaResponse(TareaCreate):
    id: int
    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# instancia fastAPI
app = FastAPI(title="API de Gestión de Tareas")


app.mount("/static", StaticFiles(directory="static"), name="static")

# web principl (ruta principl)
@app.get("/", response_class=FileResponse, tags=["Interfaz Web"])
def index():
    return "static/index.html"

# Endpoint rest api
@app.get("/tareas", response_model=List[TareaResponse], tags=["API Tareas"])
def obtener_tareas(db: Session = Depends(get_db)):
    return db.query(TareaDB).all()

@app.post("/tareas", response_model=TareaResponse, tags=["API Tareas"])
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    nueva_tarea = TareaDB(titulo=tarea.titulo, descripcion=tarea.descripcion, completada=tarea.completada)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

@app.delete("/tareas/{tarea_id}", tags=["API Tareas"])
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(TareaDB).filter(TareaDB.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(tarea)
    db.commit()
    return {"mensaje": "Eliminada correctamente"}