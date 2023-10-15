pedidos_bocadillos = ['solomo gazta', 'solomo piperrak', 'sobrasada', 'paté', 'chocolate', 'queso y anchoas']
bocadillos_terminados = []

while pedidos_bocadillos:
    bocadillo_actual = pedidos_bocadillos.pop()
    bocadillos_terminados.append(bocadillo_actual)
    print(f"\tSu bocadilo de {bocadillo_actual} está listo.")

print("\n\tHemos terminado todos los bocadillos. Estos son los bocadillos:")
for bocadillo in bocadillos_terminados:
    print(f"\t\t{bocadillo}")
