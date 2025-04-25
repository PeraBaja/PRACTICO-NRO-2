from enum import StrEnum
from pydantic import BaseModel, Field, PositiveInt, Secret, field_validator, EmailStr


class Rol(StrEnum):
    Cliente = "cliente"
    Adminstrador = "administrador"


secret_str = Secret[str]


class Usuario(BaseModel):
    id: PositiveInt
    nombre: str
    password: secret_str = Field(min_length=8)
    país: str
    ciudad: str
    teléfono: str
    dirección_correo: EmailStr
    rol: Rol

    @field_validator("password")
    def validar_primera_letra_mayusculas(value: str):
        return value[0].isupper()
