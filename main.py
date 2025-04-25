from fastapi import FastAPI
from Modelos.Producto import Producto
from Modelos.Venta import Venta
from Modelos.Usuario import Usuario
from Modelos.Venta import Venta

app = FastAPI()

productos = [
    {"id": 1, "nombre": "Teclado Mecánico", "precio": 59.99, "id_categoría": 1},
    {"id": 2, "nombre": "Monitor 24 pulgadas", "precio": 199.99, "id_categoría": 2},
    {"id": 3, "nombre": "Mouse Gamer", "precio": 29.99, "id_categoría": 1},
]

usuarios = [
    {
        "id": 1,
        "nombre": "Juan Pérez",
        "password": "Contraseña123",
        "país": "Argentina",
        "ciudad": "Buenos Aires",
        "teléfono": "+54 11 1234 5678",
        "dirección_correo": "juan.perez@email.com",
        "rol": "cliente",
    },
    {
        "id": 2,
        "nombre": "Ana López",
        "password": "AdminPass1",
        "país": "México",
        "ciudad": "CDMX",
        "teléfono": "+52 55 1234 5678",
        "dirección_correo": "ana.lopez@admin.com",
        "rol": "administrador",
    },
]
categorías = [
    {"id": 1, "descripción": "Periféricos"},
    {"id": 2, "descripción": "Monitores"},
    {"id": 3, "descripción": "Accesorios"},
]
ventas = [
    {"id": 1, "id_producto": 1, "id_usuario": 1, "cantidad": 2, "despachado": True},
    {"id": 2, "id_producto": 3, "id_usuario": 1, "cantidad": 1, "despachado": False},
    {"id": 3, "id_producto": 2, "id_usuario": 2, "cantidad": 1, "despachado": True},
]


@app.get("/")
def hello_world():
    return {"hello": "word"}


@app.get("/productos")
def obtener_productos() -> list[Producto]:
    return
