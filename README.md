🔹 1. CREAR UN ENDPOINT GET

Sirve para obtener datos.

@app.get("/jugadores")
def obtener_jugadores():
    return {"mensaje": "Lista de jugadores"}


📌 Se accede desde el navegador:

http://localhost:8000/jugadores

🔹 2. ENDPOINT CON PARÁMETROS EN LA URL
@app.get("/jugador/{id}")
def obtener_jugador(id: int):
    return {"id": id}


📌 Llamada:

/jugador/5

🔹 3. ENDPOINT POST (ENVIAR DATOS)

Usado para crear datos.

@app.post("/crear")
def crear(nombre: str = Form(...)):
    return {"nombre": nombre}


📌 Recibe datos desde un formulario HTML.

🔹 4. ENDPOINT CON BASE DE DATOS
@app.get("/jugadores")
def jugadores(db: Session = Depends(get_db)):
    return db.query(Jugador).all()


📌 Depends() inyecta la conexión.

🔹 5. DEVOLVER JSON

FastAPI devuelve JSON automáticamente:

return {"nombre": "Juan"}


Tiene formato API REST.

🔹 6. DEVOLVER HTML
return templates.TemplateResponse("index.html", {"request": request})


Sirve vistas web.

🔹 7. REDIRECCIONAR
return RedirectResponse("/", status_code=303)


Vuelve a otra URL.

🔹 8. VALIDAR FORMULARIOS
nombre: str = Form(...)


El ... obliga el campo.

🔹 9. MOSTRAR EN API (JSON REAL)
return [{"nombre": j.nombre} for j in jugadores]
