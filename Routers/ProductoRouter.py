from typing import Optional
from fastapi import APIRouter, Query, status, Body, HTTPException
from Modelos.Producto import Producto
from BD.bd import productos
from Servicios.CategoríaServicio import (
    existe_categoría_con_id,
    obtener_categoría_con_descripción,
)

router = APIRouter()


@router.get("/", tags=["Productos"], response_model=list[Producto])
def obtener_productos(nombre_categoría: Optional[str] = None) -> list[dict]:
    if nombre_categoría:
        return obtener_productos_por_categoría(nombre_categoría)
    return productos


@router.get("/{id}", tags=["Productos"], response_model=Producto)
def obtener_producto_por_id(id: int):
    for producto in productos:
        if producto["id"] == id:
            return producto
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
    )


@router.post("/", tags=["Productos"], status_code=status.HTTP_201_CREATED)
def agregar_producto(producto: Producto):
    if existe_categoría_con_id(producto.id_categoría):
        productos.append(producto.__dict__)
        return
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="No se ha podido crear. Categoría no existente",
    )


@router.put("/{id}", tags=["Productos"], response_model=Producto)
def modificar_producto(id, producto: Producto = Body()):
    producto_seleccionado = obtener_producto_por_id(id)
    try:
        i = productos.index(producto_seleccionado)
    except IndexError:
        return
    if existe_categoría_con_id(productos[i].id_categoría):
        productos[i] = producto.__dict__
        return producto.__dict__
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="No se ha podido modificar. Categoría no existente",
    )


@router.delete("/{id}", tags=["Productos"], status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(id: int):
    producto_seleccionado = obtener_producto_por_id(id)

    productos.remove(producto_seleccionado)


def obtener_productos_por_categoría(nombre_categoría: str):
    categoría = obtener_categoría_con_descripción(nombre_categoría)
    if not categoría:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no existente"
        )
    productos_filtrados = list(
        filter(lambda producto: producto["id_categoría"] == categoría["id"], productos)
    )
    if productos_filtrados:
        return productos_filtrados

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
    )
