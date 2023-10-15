numeros_favoritos = {
    'idoia': [3, 15],
    'arturo jr': [7, 8, 33],
    'nati': [4],
    'arturo sr': [8, 12],
    'alex': [2],
    'lidia': [4, 8],
    'feli': []
    }

# print(f"El número favorito de Idoia es {numeros_favoritos['idoia']}.")
# print(f"El número favorito de Arturo hijo es {numeros_favoritos['arturo jr']}.")
# print(f"El número favorito de Nati es {numeros_favoritos['nati']}.")
# print(f"El número favorito de Arturo padre es {numeros_favoritos['arturo sr']}.")
# print(f"El número favorito de Alex es {numeros_favoritos['alex']}.")
# print(f"El número favorito de Lidia es {numeros_favoritos['lidia']}.")

for persona, numeros in numeros_favoritos.items():
    persona = persona.title()
    if len(numeros) == 0:
        print(f"\n¡{persona} no tiene números favoritos!")
    elif len(numeros) == 1:
        print(f"\nEl número favorito de {persona} es {numeros[0]}")
    else:
        print(f"\nLos números favoritos de {persona} son:")
        for numero in numeros:
            print(f"\t{numero}")