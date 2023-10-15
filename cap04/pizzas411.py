pizzas = ['carbonara', 'hawaiana', 'bonita']

for pizza in pizzas:
    print(f'{pizza.title()} es una de mis pizzas favoritas')
print('\nMe encantan las pizzas. ¡Suelo comer 10 pizzas por semana!')

friend_pizzas = pizzas[:]
pizzas.append('granjera')
friend_pizzas.append('san fausto')

print('\nMis pizzas favoritas son:')

for pizza in pizzas:
    print(pizza)

print('Las pizzas favoritas de mi amigo son:')

for pizza in friend_pizzas:
    print(pizza)