#usuarios = ['carlos', 'javier', 'laura', 'arturo', 'admin', 'asun']
usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print(f"Hola, {usuario.title()}, ¿quieres ver un informe de estado?")
        else:
            print(f"Hola, {usuario.title()}, gracias por volver a entrar.")
else:
    print("¡Necesitamos encontrar algún usuario!")