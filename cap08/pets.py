def describe_pet(pet_name, animal_type='dog'):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#argumentos posicionales
describe_pet('dali', 'dog')
describe_pet('donald', 'duck')
#argumentos de palabra clave
describe_pet(animal_type='cat', pet_name='frida')
describe_pet(pet_name='donkey', animal_type='frog')
describe_pet(pet_name='argi')
describe_pet('pichón')
