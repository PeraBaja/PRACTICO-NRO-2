from fastapi import FastAPI
from Modelos.Producto import Producto
from Modelos.Venta import Venta
from Modelos.Usuario import Usuario
from Modelos.Venta import Venta
from Routers import ProductoRouter, CategoríaRouter, UsuarioRouter

app = FastAPI()

app.title = "Trabajo práctico NRO 2"
app.version = "0.0.∞"

app.router.include_router(ProductoRouter.router, prefix="/productos")
app.router.include_router(CategoríaRouter.router, prefix="/categorias")
app.router.include_router(UsuarioRouter.router, prefix="/usuarios")
