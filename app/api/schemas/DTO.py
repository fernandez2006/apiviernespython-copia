from pydantic import BaseModel, Field
from datetime import date 

#DTO
class UsuarioDTOpeticion(BaseModel):
    nombre: str
    edad: int
    telefono: str
    correo: str
    contraseña: str
    fechaRegistro:date
    cuidad: str
    class Config:
        orm_mode=True

class UsuarioDTOrespuesta(BaseModel):
    id:int
    nombre:str
    telefono:str
    cuidad:str
    class Config:
        orm_mode=True

class GastoDTOpeticion(BaseModel):
    nombre:str
    monto:float
    fecha:date
    descripcion:str
    class Config:
        orm_mode=True

class GastoDTOrespuesta(BaseModel):
    id:int
    nombre:str
    fecha:date
    monto: float
    class Config:
        orm_mode=True

class CategoriaDTOpeticion (BaseModel):
    nombreCategoria:str
    descripcion:str
    fotoIcono:str
    class Config:
        orm_mode=True

class CategoriaDTOrespuesta(BaseModel):
    id:int
    nombreCategoria:str
    fotoIcono:str
    class Config: 
        orm_mode=True

class MetodopagoDTOpeticion(BaseModel):
    nombreMetodo:str
    descripcion:str
    tipo:str
    class Config:
        orm_mode=True

class MetodopagoDTOrespuesta(BaseModel):
    id:int
    nombreMetodo:str
    descripcion:str
    class Config:
        orm_mode=True
      
class FacturaDTOpeticion(BaseModel):
    nombrevendedor:str
    fechaFactura:str
    Total:float
    descripcion:str
    class Config:
        orm_mode=True

class FacturaDTOrespuesta(BaseModel):
     id:int
     nombreVendedor:str
     Total:float
     fechaFactura:str
     descripcion:str
     class Config:
        orm_mode=True

