def hacer_camiseta(talla, texto):
    """Crea una camiseta con una talla y un mensaje concretos."""
    mensaje_1 = "Ha encargado una camiseta de la talla "
    mensaje_2 = " con el siguiente mensaje: "
    print(mensaje_1 + talla.upper() + mensaje_2 + texto + ".")

hacer_camiseta('l', 'Club de Atletismo Salinas de Pisuerga')
hacer_camiseta(texto='Club Alpino Ariz', talla='s')