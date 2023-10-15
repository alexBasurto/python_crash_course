numero = input("Escriba un número, y le diré si ese número es multiplo de 10 o no. ")
numero = int(numero)

if numero % 10 == 0:
    print(f"\nEl número {numero} es multiplo de 10.")
else:
    print(f"\nEl número {numero} no es multiplo de 10.")