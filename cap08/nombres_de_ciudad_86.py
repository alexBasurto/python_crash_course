def ciudad_pais(ciudad, pais):
    """Devuelve una cadena con el formato 'Ciudad, País'."""
    ciudadpais = f"{ciudad}, {pais}"
    return ciudadpais.title()

ciudad1 = ciudad_pais('madrid', 'españa')
print(ciudad1)
ciudad2 = ciudad_pais('parís', 'francia')
print(ciudad2)
ciudad3 = ciudad_pais('roma', 'italia')
print(ciudad3)