persona_0 = {
    'nombre': 'lidia',
    'apellido1': 'vivanco',
    'apellido2': 'de francisco',
    'edad': 34,
    'ciudad': 'basauri',
    }

persona_1 = {
    'nombre': 'alex',
    'apellido1': 'basurto',
    'apellido2': 'arana',
    'edad': 33,
    'ciudad': 'basauri',
    }

persona_2 = {
    'nombre': 'idoia',
    'apellido1': 'basurto',
    'apellido2': 'arana',
    'edad': 28,
    'ciudad': 'castro urdiales',
    }

personas = [persona_0, persona_1, persona_2]

for persona in personas:
    nombre_completo = f"{persona['nombre']} {persona['apellido1']} {persona['apellido2']}"
    nombre_completo = nombre_completo.title()
    location = persona['ciudad'].title()
    print(f"\nDatos de {nombre_completo}")
    print(f"\tEdad: {persona['edad']} años")
    print(f"\tLugar de residencia: {location}")

# print(f'Diccionario persona: {persona}')
# nombre_completo = persona['nombre'].title() + ' ' + persona['apellido1'].title() + ' ' + persona['apellido2'].title()
# edad = persona['edad']
# ciudad = persona['ciudad'].title()
# print(f'Ella es {nombre_completo}, de {edad} años de edad y vive en {ciudad}.')