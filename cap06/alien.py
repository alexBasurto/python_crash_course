#un diccionario en Python es una colección de pares clave-valor
#diccionario = {'clave1': 'valor1', ..., 'claven': 'valorn'}
#podemos almacenar como valor un número, una cadena, una lista, otro diccionario... cualquier objeto que podamos crear con Python.
#en Python un diccionario va entre llaves {}

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#podemos añadir nuevos pares clave-valor en cualquier momento

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)