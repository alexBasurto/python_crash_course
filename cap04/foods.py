my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #en esta línea estamos copiando la lista

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#friend_foods = my_foods establece que ambos nombres son LA MISMA lista.
#por lo que los añadidos posteriores se añaden a ambas listas

our_foods = ['pizza', 'falafel', 'carrot cake']
your_foods = our_foods

our_foods.append('cannoli')
your_foods.append('ice cream')

print("\nOur favorite foods are:")
print(our_foods)

print("\nYour favorite foods are:")
print(your_foods)

#ejercicio 4-12
print('\n\t\tImprimiendo listas mediante bucles:')
print('\tMis comidas favoritas:')
for food in my_foods:
    print(food.title())
print('\tComidas favoritas de mi amigo:')
for food in friend_foods:
    print(food.title())
print('\tNuestras comidas favoritas:')
for food in our_foods:
    print(food.title())
print('\tVuestras comidas favoritas:')
for food in your_foods:
    print(food.title())