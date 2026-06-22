from pydantic import BaseModel






#Crear el modelo transacciones (id, fecha, vr_total, cliente)
class FacturaBase(BaseModel):
    fecha: str
    vr_total: float # calcular(cantidad + vr_unitario)
    cliente: Cliente # esta es la relacion con el cliente(objeto)


class FacturaCrear(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None