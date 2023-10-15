def mostrar_mensajes(mensajes_borrador):
    """Muestra los mensajes de texto en borrador."""
    print("\nEstos son los mensajes de texto en borrador.")
    for mensaje in mensajes_borrador:
        print(mensaje)

def enviar_mensajes(mensajes_borrador, mensajes_enviados):
    """Envía los mensajes que están en borrador."""
    print("\nEnviando mensajes...")
    while mensajes_borrador:
        mensaje_actual = mensajes_borrador.pop()
        print(f"Enviando mensaje: {mensaje_actual}")
        mensajes_enviados.append(mensaje_actual)

mensajes_borrador = ['Voy a llegar tarde. No me esperéis.', 'Llego en 5 minutos', 'Hemos quedado en el Escaramujo', 'Ya te he hecho el Bizum.']
mensajes_enviados = []

mostrar_mensajes(mensajes_borrador)
enviar_mensajes(mensajes_borrador, mensajes_enviados)

print(mensajes_borrador)
print(mensajes_enviados)
