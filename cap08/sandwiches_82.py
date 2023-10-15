def make_sandwich(nombre, *ingredients):
    """Devuelve la composición de un sándwich."""
    print(f"\n{nombre} ha pedido un sándwich de:")
    for ingredient in ingredients:
        print(f"\t - {ingredient}")

sandwich_mario = make_sandwich('Mario', 'atún', 'cebolla', 'lechuga')
sandwich_lidia = make_sandwich('Lidia', 'pavo')
sandwich_alex = make_sandwich('Alex', 'queso havarti', 'huevo', 'jamón', 'tomate', 'lechuga')
