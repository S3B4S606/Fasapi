from fastapi import FastAPI, HTTPException, status
from enrutadores import clientes
from enrutadores import facturas
from enrutadores import transacciones

app = FastAPI()

#incluir ruta de clientes
app.include_router(clientes.rutas_clientes, tags=["Clientes"])

#incluir ruta de facturas
app.include_router(facturas.rutas_factura, tags=["Factura"])

#incluir ruta de transacciones
app.include_router(transacciones.rutas_transacciones, tags=["Transaccion"])
