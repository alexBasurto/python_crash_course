persona = {
    'nombre': 'lidia',
    'apellido1': 'vivanco',
    'apellido2': 'de francisco',
    'edad': 34,
    'ciudad': 'basauri',
}

print(f'Diccionario persona: {persona}')
nombre_completo = persona['nombre'].title() + ' ' + persona['apellido1'].title() + ' ' + persona['apellido2'].title()
edad = persona['edad']
ciudad = persona['ciudad'].title()
print(f'Ella es {nombre_completo}, de {edad} años de edad y vive en {ciudad}.')