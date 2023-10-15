archivo = "cap10\\libro_invitados.txt"

while True:
    print("Escriba 'exit' en cualquier momento para salir del programa.")
    nombre_usuario = input("Por favor, escriba su nombre: ")
    if nombre_usuario == 'exit':
        break
    apellidos_usuario = input("Ahora indique sus dos primeros apellidos: ")
    if apellidos_usuario == 'exit':
        break
    with open(archivo, 'a', encoding="utf-8") as objeto_archivo:
        objeto_archivo.write(f"{nombre_usuario.title()} {apellidos_usuario.title()}\n")