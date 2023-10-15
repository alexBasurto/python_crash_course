#3 años gratis, 3-12 años 8 euros, 12-* 12 euros
prompt = "\nPor favor, indiquenos su edad y le diremos el precio de su entrada"
prompt += "\n(Escriba 'quit' para salir del bucle) "

while True:
    edad = input(prompt)
    if edad == 'quit':
        break
    else:
        edad = int(edad)
    if edad < 3:
        print("\tPor ser menor de 3 años no tienes que pagar entrada.")
    elif edad < 12:
        print("\tEl precio de tu entrada es de 8 euros.")
    elif edad >= 12:
        print("\tEl precio de tu entrada es de 12 euros.")