from BD.bd import productos


def existe_producto_con_id(valor: int) -> bool:
    for producto in productos:
        if valor == producto["id"]:
            return True
    return False
