magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#for _____ in ____: (obligatorios los dos puntos)
#instruccion interna del bucle for.
#después de la palabra 'for' estamos declarando la variable 'magician', la cual usaremos posteriormente
#es una variable temporal. for item in list_of_items (for singular in plural)
#se considera dentro del bucle todas las lineas posteriores que tengan la correspondiente sangría
#las líneas posteriores no sangradas se ejecutan una vez, y se consideran la finalización del bucle
#indent = sangrado. Usar las sangrías solo cuando toque.

print('\n')

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can´t wait to see your next trick, {magician.title()}\n")
print("Thank you, everyone. That was a great magic show!")

#al escribir codigo, puede fallar la sintaxis o la lógica del código.
