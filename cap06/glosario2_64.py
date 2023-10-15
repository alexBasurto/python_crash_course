glosario = {
    'print' : 'es la función que permite imprimir en pantalla',
    'f': 'proviene de format, permite dar formato a cadenas de texto e insertar variables',
    '#': 'sirve para escribir comentarios en el código. Son lineas que dan contexto al desarrollador, no son ejecutadas',
    'pep8': 'guia de estilo y recomendaciones',
    'for': 'permite pasar por todos los valores de una lista o diccionario',
    'items()': 'método que devuelve los pares clave-valor de un diccionario',
    'keys()': 'método que devuelve las claves de un diccionario',
    'values()': 'método que devuelve los valores de un diccionario',
    '+': 'carácter para concatenar cadenas',
    ':,': 'para devolver un número con separador de miles',
    }

# print("\nprint:")
# print(f"\n\t{glosario['print'].capitalize()}")

# print("\nf:")
# print(f"\n\t{glosario['f'].capitalize()}")

# print("\n#:")
# print(f"\n\t{glosario['#'].capitalize()}")

# print("\npep8:")
# print(f"\n\t{glosario['pep8'].capitalize()}")

# print("\nfor:")
# print(f"\n\t{glosario['for'].capitalize()}")

#otra forma de hacerlo, con un bucle for:
for key, value in glosario.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")