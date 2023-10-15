message = "Me encantan los gatos."
print(message)
print(message.replace('gatos', 'perros'))
print(message)

file = "cap10\\aprender_python.txt"

#Leyendo el archivo completo:
with open(file, encoding="utf-8") as file_object:
    contenido = file_object.read()
    print("\nLeyendo el archivo completo:")
    print(contenido.replace('Python', 'C#'))

#Pasando en bucle por el objeto del archivo:
with open(file, encoding="utf-8") as file_object:
    print("\nLeyendo línea por línea:")
    for line in file_object:
        print(line.rstrip().replace('Python', 'C#'))

#Guardando las líneas en una lista para trabajar con ellas fuera del bloque with:
with open(file, encoding="utf-8") as file_object:
    lines = file_object.readlines()


print("\nExtrayendo a una lista, para trabajar fuera del bloque WITH:")
for line in lines:
    print(line.rstrip().replace('Python', 'C#'))