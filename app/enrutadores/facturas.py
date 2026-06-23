from fastapi import APIRouter, HTTPException, status
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.clientes import Cliente
from listas import Lista_clientes, Lista_facturas

rutas_factura = APIRouter()
#Lista_facturas: list[Factura] = [] 
#Lista_clientes: list[Cliente] = []


@rutas_factura.get("/facturas/", response_model=list[Factura])
async def listar_factura():
    return Lista_facturas



@rutas_factura.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    #recorrer la lista_facturas
    for i, obj_factura in enumerate(Lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"La factura con id {factura_id} no existe."
    )


@rutas_factura.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):
    #buscar el cliente
    cliente_encontrado = None
    for cliente in Lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
    # mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El cliente con id {cliente_id} no existe"
        )

    #validar datos de la factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    #id de la factura
    factura_val.id = len(Lista_facturas) + 1
    Lista_facturas.append(factura_val)
    return factura_val


@rutas_factura.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass


@rutas_factura.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass