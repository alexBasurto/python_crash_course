cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
#orden alf. sort
print(cars)
#orden alf. inverso, sort + reverse
cars.sort(reverse=True)
print(cars)
#con el metodo sort los cambios son permanentes, se hacen en la propia lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n\tHere is the original list:")
print(cars)
#ordenar una lista temporalmente, sorted
print("\n\tHere is the sorted list:")
print(sorted(cars))
print("\n\tHere is the original list again:")
print(cars)
print("\n\tAquí la lista original invirtiendo el orden original (permanente):")
cars.reverse()
print(cars)
#longitud (cantidad de valores almacenados en la lista. empieza desde 1 y no desde 0).
print(f'{len(cars)} coches') #4 coches
