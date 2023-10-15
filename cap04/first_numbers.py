for value in range(1, 5): #imprimirá los números del 1 al 4. El 5 no lo imprime.
    #Se detiene al llegar a 5, sin ejecutar el interior del bucle.
    print(value)

for value in range(1, 6):
    print(value)

#si pasamos un único valor, empieza en cero y termina en dicho valor
for value in range(4):
    print(value)

print('\n\tUso de range()')
#usar range() para hacer una lista de números

numbers = list(range(1, 6))# lo mismo que poner numbers = list([1, 2, 5])
print(numbers)