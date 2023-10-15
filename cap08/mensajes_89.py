def mostrar_mensajes(mensajes):
    """Muestra los mensajes de texto enviados hoy."""
    print("\nEstos son los mensajes de texto enviados hoy.")
    for mensaje in mensajes:
        print(mensaje)

mensajes = ['Voy a llegar tarde. No me esperéis.', 'Llego en 5 minutos', 'Hemos quedado en el Escaramujo', 'Ya te he hecho el Bizum.']
mostrar_mensajes(mensajes)