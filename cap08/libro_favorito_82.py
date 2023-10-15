def libro_favorito(titulo, autor):
    """Muestra uno de los libros favoritos del usuario."""
    mensaje_pt1 = "Uno de mis libros favoritos es "
    print(mensaje_pt1 + titulo.title() + ", de " + autor.title() + ".")

libro_favorito("los pilares de la tierra", "Ken Follet")