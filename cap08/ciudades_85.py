def descubrir_ciudad(ciudad, pais = 'España'):
    """Indica una ciudad y su país."""
    print(ciudad.title() + " está en " + pais.title() + ".")

descubrir_ciudad('bilbao', 'españa')
descubrir_ciudad('madrid')
descubrir_ciudad('san francisco', 'estados unidos')
