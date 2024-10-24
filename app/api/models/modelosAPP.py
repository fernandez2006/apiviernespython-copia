from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#crear una instancia de la base para crear tablas
base=declarative_base()

#listado de modelos de la aplicacion 
#usario
class Usuario(base):
    __tablename__='usuarios'
    id= Column (Integer, primary_key=True, autoincrement=True)
    nombre= Column (String(50))
    edad= Column (Float)
    telefono= Column (String(12))
    Correo= Column (String(50))
    contraseña= Column (String(30))
    fechaRegistro=Column (Date)
    cuidad= Column (String(50))

#GASTO
class Gasto (base):
    __tablename__='gastos'
    id= Column (Integer, primary_key=True, autoincrement=True)
    nombre=Column (String (100))
    monto= Column (Float)
    fecha= Column (Date)
    descripcion= Column (100)

#CATEGORIA
class Categoria(base):
    __tablename__='categoria'
    id= Column (Integer,primary_key=True, autoincrement=True)
    nombreCategoria= Column (String(20))
    descripcion= Column(String(100))
    fotoIcono= Column (String(100))

#METODOS DE PAGO 
class MetodoPago (base):
    __tablename__='metodopago'
    id= Column (Integer, primary_key=True, autoincrement=True)
    nombreMetodo= Column (String (50))
    tipo= Column (String(50))
    descripcion= Column (String(100))

#FACTURA
class Factura (base):
    __tablename__='factura'
    id= Column (Integer, primary_key=True, autoincrement=True)
    nombreVendedor= Column (String (30))
    fechaFactura= Column (Date)
    Total= Column (Float)
    descripcion= Column (String(100))
    

