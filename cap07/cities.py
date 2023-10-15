prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#un bucle while con condición True se ejecutará eternamente,
#hasta que encuentre una orden break
#break se puede usar con cualquier bucle de python, también for