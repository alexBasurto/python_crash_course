prompt = "\nPor favor, indique los ingredientes que desea para su pizza."
prompt += "\n(Escriba 'quit' cuando quiera cerrar el programa) "
ingrediente = input(prompt)
active = True

while active:
    if ingrediente != 'quit':
        ingrediente = input(f"\nDe acuerdo, {ingrediente}. ¿Qué más? ")
    elif ingrediente == 'quit':
        active = False