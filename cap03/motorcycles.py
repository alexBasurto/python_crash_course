#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#así sustituimos honda por ducati
#motorcycles[0] = 'ducati'
#print(motorcycles)

#así añadimos un nuevo valor a la lista
#motorcycles.append('ducati')
#print(motorcycles)

#así empezamos con una lista vacía y vamos añadiendo valores, append
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('bmw')
motorcycles.append('rieju')
motorcycles.append('kawasaki')

print("Usando append:")
print(motorcycles)

#insertar valores, desplazando el resto, insert

motorcycles.insert(0, 'ducati')
print("Usando insert:")
print(motorcycles)

#eliminar elementos, del
del motorcycles[0]
print("Usando del:")
print(motorcycles)

#Eliminar último elemento con método pop()
popped_motorcycles = motorcycles.pop()
print("Usando el método pop():")
print("Hemos eliminado el último elemento de la lista:")
print(motorcycles)
print("Pero lo tenemos guardado en una variable llamada popped_motorcycles:")
print(popped_motorcycles)

#Eliminar elemento determinado con método pop()
first_owned = motorcycles.pop(0)
print("Usando el método pop(0) con una posición determinada")
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Usamos del para no volver a usar jamás un elemento, y pop en caso de que queramos usarlo.

#Eliminar un elemento por valor (p.e. bmw)
motorcycles.remove('bmw')
print("Usando remove()")
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")