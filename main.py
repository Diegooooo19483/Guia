from fastapi import FastAPI, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Jugador
import models

app = FastAPI(title="Mini Fútbol API")

# Crear tablas cuando arranca la app
Base.metadata.create_all(bind=engine)

# Templates
templates = Jinja2Templates(directory="templates")

# Dependencia de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ HOME
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    jugadores = db.query(Jugador).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "jugadores": jugadores
    })


# ✅ FORMULARIO
@app.get("/form")
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


# ✅ CREAR JUGADOR
@app.post("/crear")
def crear(
    nombre: str = Form(...),
    edad: int = Form(...),
    posicion: str = Form(...),
    db: Session = Depends(get_db)
):
    jugador = Jugador(
        nombre=nombre,
        edad=edad,
        posicion=posicion
    )

    db.add(jugador)
    db.commit()

    return RedirectResponse("/", status_code=303)


# ✅ API JSON
@app.get("/api/jugadores")
def api_jugadores(db: Session = Depends(get_db)):
    jugadores = db.query(Jugador).all()

    return [
        {
            "id": j.id,
            "nombre": j.nombre,
            "edad": j.edad,
            "posicion": j.posicion,
            "goles": j.goles
        }
        for j in jugadores
    ]
