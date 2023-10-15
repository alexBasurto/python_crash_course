comensales = input("Disculpe, caballero. ¿Cuántas personas serán a la mesa? ")
comensales = int(comensales)

if comensales > 8:
    print("\nTendrán que esperar 20 minutos. Pueden esperar en la barra.")
else:
    print("\nSu mesa esta lista. Sígame.")