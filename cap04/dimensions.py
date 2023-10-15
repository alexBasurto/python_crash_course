#tupla = lista de elementos que no se puede alterar.
#En python, cuando algo no se puede cambiar (constante) lo llamamos inmutable.
dimensions = (200, 50) #la dupla usa parentesis en vez de corchetes.
print(dimensions[0])
print(dimensions[1])
#veamos el fallo al tratar de modificar el elemento con indice 0
#dimensions[0] = 150
my_t = (3,) #si la tupla tiene un único elemento, hay que ponerle una coma final.

print('Imprimir elementos de la tupla con un bucle for:')
for dimension in dimensions:
    print(dimension)

print('No podemos modificar tuplas, pero si cambiar todos sus elementos a posteriori:')
dimensions = (400, 100)
print('\nDimensiones modificadas:')
for dimension in dimensions:
    print(dimension)

#usamos las tuplas cuando los valores van a ser fijos durante toda la ejecución del programa.
