from enum import StrEnum
from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    field_validator,
    EmailStr,
    SecretStr,
)


class Rol(StrEnum):
    Cliente = "cliente"
    Adminstrador = "administrador"


class Usuario(BaseModel):
    id: PositiveInt
    nombre: str
    password: SecretStr
    país: str
    ciudad: str
    teléfono: str
    dirección_correo: EmailStr
    rol: Rol

    @field_validator("password")
    def validar_al_menos_una_letra_mayusculas(cls, valor: SecretStr):
        if valor.get_secret_value().islower():
            raise ValueError("Debe contener al menos una letra mayuscula")
        return valor

    @field_validator("password")
    def validar_longitud_minima_contraseña(cls, valor: SecretStr):
        if len(valor.get_secret_value()) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caraceres")
        return valor
