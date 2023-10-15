archivo = "cap10\\encuesta_programacion.txt"

while True:
    print("Escriba 'exit' en cualquier momento para salir del programa.")
    respuesta = input("Por favor, indique un motivo por el que le gusta programar: ")
    if respuesta == 'exit':
        break
    with open(archivo, 'a', encoding="utf-8") as objeto_archivo:
        objeto_archivo.write(f"{respuesta.capitalize()}\n")