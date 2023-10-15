brands = ['peugeot', 'citroen', 'renault', 'opel']
car_model1 = 'Peugeot 208'
antiguedad_1 = 8
car_model2 = 'Peugeot 508'
antiguedad_2 = 6
car_model3 = 'peugeot 208'
antiguedad_3 = 10
print("car_model1 y car_model2 coinciden? Predigo que False")
print(car_model1 == car_model2)

print("\ncar_model1 y car_model3 coinciden? Predigo que False")
print(car_model1 == car_model3)

print("\n¿Y si no tengo en cuenta mays-mins? Predigo que True")
print(car_model1.lower() == car_model3.lower())

print("\nCosa que no sucede comparando car_model1 y car_mocel2. Predigo que False")
print(car_model1.lower() == car_model2.lower())

print("\nCoche 1 y 2 son igual de viejos? Predigo que False")
print(antiguedad_1 == antiguedad_2)

print("\nCoche 1 es más viejo que coche 2? Predigo que True")
print(antiguedad_1 > antiguedad_2)

print("\nCoche 2 es igual o más nuevo que coche 3. Predigo que True")
print(antiguedad_2 <= antiguedad_3)

print("\nEl primer coche es un Peugeot 208 y tiene más de 3 años. Predigo que True")
print((car_model1.lower() == 'peugeot 208') and (antiguedad_1 > 3))

print("\nCoche 2 es un Peugeot 508 o tiene más de 20 años de antiguedad. Predigo True")
print((car_model2.lower() == 'peugeot 508') or (antiguedad_2 > 20))

print("\nEstá la marca Opel en la lista brands? Predigo que True")
print('opel' in brands)

print("\nNo está la marca Skoda en la lista brands? Predigo que True")
print('skoda' not in brands)