from fastapi import APIRouter, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from listas import Lista_clientes

rutas_clientes = APIRouter()
#Lista_cliente: list[Cliente] = []


#endpoint, para obtener o listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return Lista_clientes


#endpoint, para obtener o listar un solo cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(Lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id} no existe."
    )


#endpoint, para crear un cliente, y agregar a la lista
@rutas_clientes.post("/clientes/", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar el id
    id_ciente = len(Lista_clientes)+1
    cliente_val.id = id_ciente
    Lista_clientes.append(cliente_val)
    return cliente_val


#endpoint, para editar un cliente, y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(Lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            Lista_clientes[i] = cliente_val
            return obj_cliente
    raise HTTPException(
        status_code=400,detail=f"El cliente con id {cliente_id}, no existe"
        )



# endpoint para eliminar un cliente de la lista
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(Lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = Lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
    )