mensaje = "\nPor favor, indique dos números para que sean sumados:"
print(mensaje)
try:
    numero_1 = int(input("Indique el primer número: "))
    numero_2 = int(input("Indique el segundo número: "))
except ValueError:
    print("Solo se admiten caracteres numéricos.")
else:
    resultado = numero_1 + numero_2
    print(resultado)