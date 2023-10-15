ciudades = {
    'madrid' : {
        'pais': 'españa',
        'poblacion': 3_200_000,
        'dato_curioso': 'ambiente canalla',
        },
    'berlín' : {
        'pais': 'alemania',
        'poblacion': 3_770_000,
        'dato_curioso': 'ciudad gay friendly',
        },
    'londres' : {
        'pais': 'inglaterra',
        'poblacion': 8_630_000,
        'dato_curioso': 'fish and chips',
        },
    }

for ciudad, datos in ciudades.items():
    ciudad = ciudad.title()
    pais = datos['pais'].title()
    poblacion = datos['poblacion']
    dato_curioso = datos['dato_curioso']
    print(f"Información de la ciudad de {ciudad}:")
    print(f"\tPaís: {pais}.")
    print(f"\tPoblación: {poblacion:,}")
    print(f"\tCuriosidades: {dato_curioso}.")