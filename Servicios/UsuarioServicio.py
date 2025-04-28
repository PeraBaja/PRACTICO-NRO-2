from BD.bd import usuarios


def existe_usuario_con_id(valor: int) -> bool:
    for usuario in usuarios:
        if valor == usuario["id"]:
            return True
    return False
