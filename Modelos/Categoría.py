from pydantic import BaseModel, Field, PositiveInt, field_validator


class Categoría(BaseModel):
    id: PositiveInt
    descripción: str = Field(min_length=1)

    @field_validator("descripción")
    def validar_descripción_en_blanco(cls, valor: str):
        if valor.isspace():
            raise ValueError("La descripción no debe estar vacía")
        return valor
