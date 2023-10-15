def hacer_album(nombre_artista, titulo_album):
    """Crea un diccionario para describir un album musical."""
    album = {'artista': nombre_artista, 'titulo': titulo_album}
    return album

while True:
    print("\nPor favor, indiqueme el nombre de un artista y el nombre de uno de sus álbumes:")
    print("(Introduzca 'q' para finalizar el programa)")
    artista = input("Nombre del artista: ")
    if artista == 'q':
        break
    album = input("Título del álbum: ")
    if album == 'q':
        break
    artista_album = hacer_album(artista, album)
    print(artista_album)


