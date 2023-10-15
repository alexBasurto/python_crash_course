car = 'peugeot'
model = '208'
print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')

print("\nIs car == 'peugeot'? I predict True")
print(car == 'peugeot')

print("\nIs car == 'peugeot' and model == '208'? I predict True")
print((car == 'peugeot') and (model == '208'))

print("\nIs car == 'peugeot' and model = '5008'? I predict False")
print((car == 'peugeot') and (model == '5008'))

print("\nIs car == 'renault' or car == 'citroen'? I predict False")
print((car == 'renault') or (car == 'citroen'))

print("\nIs car == 'renault' or car == 'peugeot'? I predict True")
print((car == 'renault') or (car == 'peugeot'))

print("\nIs model == '308' or model == '208'? I predict True")
print((model == '308') or (model == '208'))

pizzas = ['carbonara', 'hawaiana', 'barbacoa']
print("\nIs 'bonita' in pizzas? I predict False")
print('bonita' in pizzas)

print("\nIs 'carbonara' in pizzas? I predict True")
print('carbonara' in pizzas)

print("\nIs 'carbonara' in pizzas and 'cuatro quesos' in pizzas? I predict False")
print(('carbonara' in pizzas) and ('cuatro quesos' in pizzas))