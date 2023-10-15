rios = {
    'danubio': 'alemania',
    'tajo': 'españa',
    'loira': 'francia',
    }

for rio, pais in rios.items():
    print(f"El {rio.title()} discurre por {pais.title()}")

print("\nEstos son los ríos:")
for rio in rios.keys():
    print(rio.title())

print("\nEstos son los paises:")
for pais in rios.values():
    print(pais.title())