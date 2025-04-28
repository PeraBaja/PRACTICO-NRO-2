from fastapi import APIRouter, status, Body, HTTPException
from Modelos.Venta import Venta
from BD.bd import ventas
from Servicios.ProductoServicio import existe_producto_con_id
from Servicios.UsuarioServicio import existe_usuario_con_id

router = APIRouter()


@router.get("/", tags=["Ventas"], response_model=list[Venta])
def obtener_ventas() -> list[dict]:
    return ventas


@router.get("/{id}", tags=["Ventas"], response_model=Venta)
def obtener_venta_por_id(id: int):
    for venta in ventas:
        if venta["id"] == id:
            return venta
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrado"
    )


@router.post("/", tags=["Ventas"], status_code=status.HTTP_201_CREATED)
def agregar_venta(venta: Venta):
    if not existe_usuario_con_id(venta["id_usuario"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no existente"
        )
    elif not existe_producto_con_id(venta["id_producto"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Producto no existente"
        )

    ventas.append(venta.__dict__)


@router.patch("/{id}", tags=["Ventas"], response_model=Venta)
def marcar_como_despachado(id: int):
    venta = obtener_venta_por_id(id)
    venta["despachado"] = True
    # Aquí tendría que guardar el cambio en una base de datos pero
    # como no hay persistencia solo modifico el estado del objeto en memoria
    return venta  # Qué es mejor aquí profe? Devolver 204 No Content o devolver el recurso modificado?
