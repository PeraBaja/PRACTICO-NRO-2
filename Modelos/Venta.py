from pydantic import BaseModel, PositiveInt


class Venta(BaseModel):
    id: PositiveInt
    id_producto: PositiveInt
    id_usuario: PositiveInt
    cantidad: PositiveInt
    despachado: bool
