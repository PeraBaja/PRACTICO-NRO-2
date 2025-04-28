from http.client import HTTPException
from fastapi import APIRouter, status, Body
from Modelos.Categoría import Categoría
from BD.bd import categorías

router = APIRouter()


# Lo hago así profe para que esté más ordenado


@router.get("/", tags=["Categorías"], response_model=list[Categoría])
def obtener_categorías() -> list[dict]:
    return categorías


@router.get("/{id}", tags=["Categorías"], response_model=Categoría)
def obtener_categoría_por_id(id: int):
    for categoría in categorías:
        if categoría["id"] == id:
            return categoría
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrado"
    )


@router.post("/", tags=["Categorías"], status_code=status.HTTP_201_CREATED)
def agregar_categoría(categoría: Categoría):
    categorías.append(categoría.__dict__)


@router.put("/{id}", tags=["Categorías"], response_model=Categoría)
def modificar_categoría(id, categoría: Categoría = Body()):
    categoría_seleccionado = obtener_categoría_por_id(id)
    try:
        i = categorías.index(categoría_seleccionado)
    except IndexError:
        return

    categorías[i] = categoría.__dict__
    return categoría.__dict__


@router.delete("/{id}", tags=["Categorías"], status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoría(id: int):
    categoría_seleccionado = obtener_categoría_por_id(id)

    categorías.remove(categoría_seleccionado)
