from BD.bd import categorías


def existe_categoría_con_id(valor: int) -> bool:
    for categoría in categorías:
        if valor == categoría["id"]:
            return True
    return False
