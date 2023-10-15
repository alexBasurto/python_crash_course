#Hace una lista vacía para guardar aliens.
aliens = []

#Hace 30 aliens verdes.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Muestra los 5 primeros aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

#Muestra cuántos aliens se han creado.
print(f"Total number of aliens: {len(aliens)}.")

#Para poder pasar bucles por los diccionarios, es importante que compartan una estructura idéntica