from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosAPP import Usuario, base
from app.api.routes.rutas import rutas

from starlette.responses import RedirectResponse
# activar el ORM
base.metadata.create_all (bind=engine)
#variable para administrar la aplicacion 
app=FastAPI()

#activo el API
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)
