from pydantic import BaseModel, PositiveFloat, PositiveInt


class Producto(BaseModel):
    id: PositiveInt
    nombre: str
    precio: PositiveFloat
    id_categoría: PositiveInt
