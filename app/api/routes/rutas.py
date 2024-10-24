from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOpeticion, UsuarioDTOrespuesta
from app.api.schemas.DTO import GastoDTOpeticion, GastoDTOrespuesta
from app.api.schemas.DTO import CategoriaDTOpeticion, CategoriaDTOrespuesta
from app.api.schemas.DTO import MetodopagoDTOpeticion, MetodopagoDTOrespuesta
from app.api.schemas.DTO import FacturaDTOpeticion, FacturaDTOrespuesta
from app.api.models.modelosAPP import Usuario, Gasto, Categoria, Metodopago, Factura
from app.database.configuration import sessionLocal, engine

#para que un api funcione debe tener un archivo enrutador 
rutas=APIRouter () #ENDPOINTS

#crear una funcion para establecer cuando yo quiera y necesite 
# conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#programacion para cada uno de los servicio 
#que ofrecera nuestra api


#servicio para guardando o resgistrando un usuario en base de datos
@rutas.post("/usuarios", response_model=UsuarioDTOrespuesta)
def guardarUsuario( datosPeticion:UsuarioDTOpeticion, db:Session=Depends(getDataBase)):
    try:
        usuario=Usuario(
            nombre=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            cuidad=datosPeticion.cuidad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail=f"ERROR AL REGISTRAR EL USUARIO{error}")

@rutas.get("/usuarios", response_model= List[UsuarioDTOrespuesta])
def buscarUsarios (db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return listadoDeUsuarios
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400,detail=f"ERROR AL BUSCAR EL USUARIO {error}")

@rutas.post("/gastos", response_model=GastoDTOrespuesta)
def guardarGasto(datospeticion: GastoDTOpeticion, db: Session = Depends(getDataBase)):
    try:
        gasto = Gasto(
            nombre=datospeticion.nombre,
            monto=datospeticion.monto,
            fecha=datospeticion.fecha,
            descripcion=datospeticion.descripcion
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return gasto
    except Exception  as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL REGISTRAR EL GASTO {error}")


@rutas.get("/gastos", response_model=List[GastoDTOrespuesta])
def buscarGastos(db: Session = Depends(getDataBase)):
    try:
        listadoDeGastos = db.query(Gasto).all()
        return listadoDeGastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL BUSCAR LOS GASTOS {error}")

@rutas.post("/categoria", response_model=CategoriaDTOrespuesta)
def guardarCategoria(datospeticion: CategoriaDTOpeticion, db: Session = Depends(getDataBase)):
    try:
        categoria=Categoria(
            nombreCategoria=datospeticion.nombreCategoria,
            descripcion=datospeticion.descripcion,
            fotoIcono=datospeticion.fotoIcono
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL REGISTRAR LA CATEGORÍA {error}")

@rutas.get("/categorias", response_model=List[CategoriaDTOrespuesta])
def buscarCategorias(db: Session = Depends(getDataBase)):
    try:
        listadoDeCategorias = db.query(Categoria).all()
        return listadoDeCategorias
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL BUSCAR LAS CATEGORÍAS {error}")


@rutas.post("/metodopago", response_model=MetodopagoDTOrespuesta)
def guardarMetodopago(datospeticion: MetodopagoDTOpeticion, db: Session = Depends(getDataBase)):
    try:
        metodopago = Metodopago(
            nombreMetodo=datospeticion.nombreMetodo,
            descripcion=datospeticion.descripcion,
            tipo=datospeticion.tipo
        )
        db.add(metodopago)
        db.commit()
        db.refresh(metodopago)
        return metodopago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL REGISTRAR EL MÉTODO DE PAGO {error}")

@rutas.get("/metodopago", response_model=List[MetodopagoDTOrespuesta])
def buscarMetodosPago(db: Session = Depends(getDataBase)):
    try:
        listadoDeMetodoPago = db.query(Metodopago).all()
        return listadoDeMetodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL BUSCAR LOS MÉTODOS DE PAGO {error}")


@rutas.post("/factura", response_model=FacturaDTOrespuesta)
def guardarFactura(datospeticion: FacturaDTOpeticion, db: Session = Depends(getDataBase)):
    try:
        factura = Factura(
            nombreVendedor=datospeticion.nombreVendedor,
            Total=datospeticion.Total,
            fechaFactura=datospeticion.fechaFactura,
            descripcion=datospeticion.descripcion
        )
        db.add(factura)
        db.commit()
        db.refresh(factura)
        return factura
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL REGISTRAR LA FACTURA {error}")

@rutas.get("/factura", response_model=List[FacturaDTOrespuesta])
def buscarFactura(db: Session = Depends(getDataBase)):
    try:
        listadoDeFactura = db.query(Factura).all()
        return listadoDeFactura
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"ERROR AL BUSCAR LAS FACTURAS {error}")

