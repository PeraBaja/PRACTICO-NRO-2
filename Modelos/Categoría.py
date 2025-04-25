from pydantic import BaseModel, PositiveInt


class Categoría(BaseModel):
    id: PositiveInt
    descripción: str
