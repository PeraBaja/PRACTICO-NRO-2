from fastapi import APIRouter, status, Body, HTTPException
from Modelos.Usuario import Usuario
from BD.bd import usuarios
from Servicios.CategoríaServicio import existe_categoría_con_id

router = APIRouter()


@router.get("/", tags=["Usuarios"], response_model=list[Usuario])
def obtener_usuarios() -> list[dict]:
    return usuarios


@router.get("/{id}", tags=["Usuarios"], response_model=Usuario)
def obtener_usuario_por_id(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
    )


@router.post("/", tags=["Usuarios"], status_code=status.HTTP_201_CREATED)
def agregar_usuario(usuario: Usuario):
    usuarios.append(usuario.__dict__)


@router.put("/{id}", tags=["Usuarios"], response_model=Usuario)
def modificar_usuario(id, usuario: Usuario = Body()):
    usuario_seleccionado = obtener_usuario_por_id(id)
    try:
        i = usuarios.index(usuario_seleccionado)
    except IndexError:
        usuarios[i] = usuario.__dict__
        return usuario.__dict__


@router.delete("/{id}", tags=["Usuarios"], status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(id: int):
    usuario_seleccionado = obtener_usuario_por_id(id)
    usuarios.remove(usuario_seleccionado)
