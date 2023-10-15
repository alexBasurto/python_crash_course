# ejercicio 11.1

def formato_ciudad_pais(ciudad, pais, habitantes=''):
    if habitantes:
        resultado = f'{ciudad.title()}, {pais.title()} - habitantes {habitantes}.'
    else:
        resultado = f'{ciudad.title()}, {pais.title()}.'
    return resultado

#print(formato_ciudad_pais('Bilbao', 'España', 5))
