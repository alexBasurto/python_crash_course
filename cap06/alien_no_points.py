alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) #KeyError: 'points'

point_value = alien_0.get('points', 'No point value assigned.') #metodo .get('clave buscada', 'resultado si fallo'). Si no rellenamos el segundo valor, devolverá el valor 'none'.
print(point_value)


alien_1 = {'color': 'yellow', 'speed': 'fast', 'points': 10}
point_value = alien_1.get('points', 'No point value assigned.')
print(point_value)