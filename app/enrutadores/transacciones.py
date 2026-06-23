from fastapi import APIRouter, HTTPException, status
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from modelos.facturas import Factura
from listas import Lista_facturas, Lista_transacciones

rutas_transacciones = APIRouter()
#Lista_transacciones: list[Transaccion] = []
#Lista_facturas: list[Factura] =  []


@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return Lista_transacciones


@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transacciones(id_transaccion: int):
    pass


@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: Transaccion):
    #buscar la factura
    factura_encontrada = None
    for factura in Lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
    # mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"La factura con id {factura_id}, no existe.",
        )
    
    #validar datos de la transaccion
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    factura_encontrada.transacciones.append(transaccion_val)
    # id de la transaccion
    transaccion_val.id = len(Lista_transacciones) + 1
    # falto agregar a la lista transaccion
    Lista_transacciones.append(transaccion_val)
    return transaccion_val


@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion):
    pass