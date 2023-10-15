mascotas = []

mascota_0 = {
    'nombre': 'argi',
    'tipo': 'perro',
    'raza': 'jack russel terrier',
    'sexo': 'hembra',
    'edad': 5,
    'dueño': 'lidia',
    }
mascota_1 = {
    'nombre': 'musgo',
    'tipo': 'perro',
    'raza': 'cazador de patos de nueva escocia',
    'sexo': 'macho',
    'edad': 3,
    'dueño': 'patri',
    }
mascota_2 = {
    'nombre': 'kika',
    'tipo': 'pajaro',
    'raza': 'agaporni',
    'sexo': 'hembra',
    'edad': 9,
    'dueño': 'raquel',
    }
mascota_3 = {
    'nombre': 'daisy',
    'tipo': 'pato',
    'raza': 'pato inglés',
    'sexo': 'hembra',
    'edad': 0,
    'dueño': 'idoia',
    }

mascotas.append(mascota_0)
mascotas.append(mascota_1)
mascotas.append(mascota_2)
mascotas.append(mascota_3)

for mascota in mascotas:
    nombre = mascota['nombre'].title()
    dueño = mascota['dueño'].title()
    print(f"\nLa mascota {nombre} es un {mascota['tipo']} y su dueñ@ es {dueño}")

