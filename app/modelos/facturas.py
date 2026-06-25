from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime






#Crear el modelo transacciones (id, fecha, vr_total, cliente)
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
    #cliente: Cliente # esta es la relacion con el cliente(objeto)
    #transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_tota(self) -> float:
        # calcular(cantidad + vr_unitario)
        # consultare id actual de factura
        #factura_id_acual = getattr(self, "id", None)
        #total_factura = 0.0
        #if not factura_id_acual or not self.transacciones:
        #    return total_factura
        #recorrer la lista transacciones, segun el factura_id
        #for transaccion in self.transacciones:
        #    if transaccion.factura_id == factura_id_acual:
        #        total_factura += Transaccion.vr_unitario + Transaccion.cantidad

        return 0.0
    

class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    Cliente_id: int = Field(default=None, foreign_key="cliente.id")
    