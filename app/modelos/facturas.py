from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime






#Crear el modelo transacciones (id, fecha, vr_total, cliente)
class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente # esta es la relacion con el cliente(objeto)
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_tota(self) -> float:
        # calcular(cantidad + vr_unitario)
        return 222    

class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None
