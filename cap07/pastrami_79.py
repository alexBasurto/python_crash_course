pedidos_bocadillos = ['solomo gazta', 'pastrami', 'pastrami', 'solomo piperrak', 'sobrasada', 'pastrami',
                      'paté', 'chocolate', 'queso y anchoas']
bocadillos_terminados = []

print("\tLo sentimos mucho, no nos quedan bocadillos de pastrami...\n")

while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')

while pedidos_bocadillos:
    bocadillo_actual = pedidos_bocadillos.pop()
    bocadillos_terminados.append(bocadillo_actual)
    print(f"\tSu bocadilo de {bocadillo_actual} está listo.")

print("\n\tHemos terminado todos los bocadillos. Estos son los bocadillos:")
for bocadillo in bocadillos_terminados:
    print(f"\t\t- {bocadillo}")
