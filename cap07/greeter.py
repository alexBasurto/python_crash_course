# name = input("Please enter your name: ")
# print(f"\nHello {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"\nHello {name}!")

#input almacena los datos numéricos como cadenas. Para evitarlo, usamos la función int()