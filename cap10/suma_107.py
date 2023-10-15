mensaje = "\nPor favor, indique dos números para que sean sumados:"
mensaje += "\nIntroduzca 'q' para salir del programa."

while True:
    print(mensaje)
    numero_1 = input("Indique el primer número: ")
    if numero_1 == 'q': break
    numero_2 = input("Indique el segundo número: ")
    if numero_2 == 'q': break
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    except ValueError:
        print("Solo se admiten caracteres numéricos.")
    else:
        resultado = numero_1 + numero_2
        print(resultado)