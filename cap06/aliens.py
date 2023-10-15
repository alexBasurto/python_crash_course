#creando una lista de diccionarios. Primero creo los diccionarios...
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#...y después creo la lista que los contiene:
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)