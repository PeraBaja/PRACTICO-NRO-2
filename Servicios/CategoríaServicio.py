from BD.bd import categorías


def existe_categoría_con_id(valor: int) -> bool:
    for categoría in categorías:
        if valor == categoría["id"]:
            return True
    return False


def obtener_categoría_con_descripción(valor: int) -> bool:
    for categoría in categorías:
        if valor == categoría["descripción"]:
            return categoría
