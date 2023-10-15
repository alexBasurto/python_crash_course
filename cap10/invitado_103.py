nombre_usuario = input("Por favor, escriba su nombre: ")
apellidos_usuario = input("Ahora indique sus dos primeros apellidos: ")
archivo = "cap10\\invitado.txt"

with open(archivo, 'w', encoding="utf-8") as objeto_archivo:
    objeto_archivo.write(f"{nombre_usuario.title()} {apellidos_usuario.title()}\n")