def hacer_album(nombre_artista, titulo_album, numero_canciones=None):
    """Crea un diccionario para describir un album musical."""
    album = {'artista': nombre_artista, 'titulo': titulo_album}
    if numero_canciones:
        album['canciones'] = numero_canciones
    return album

album1 = hacer_album('Imagine Dragons', "It's Time", 14)
print(album1)
album2 = hacer_album('berri txarrak', 'ikasten')
print(album2)
album3 = hacer_album(titulo_album='agenda oculta', nombre_artista='riot propaganda')
print(album3)