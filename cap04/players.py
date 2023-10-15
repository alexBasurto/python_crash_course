#trozos o slices en las listas
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #elem del 0 al 2 (se detiene en el 3)
print(players[1:4]) #elem del 1 al 3 (se detiene en el 4)
print(players[:4]) #lo mismo que 0:4
print(players[2:]) #lo mismo que 2:0
print(players[-3:]) #muestra los 3 últimos de la lista
print(players[0:4:2]) #el tercer número indica cuantos elementos salta cada vez

#pasamos por los 3 primeros elem con un bucle for e imprimimos sus nombres
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

