montañas = ['espigüete', 'prieta', 'murcia', 'redonda', 'valdecebollas', 'curavacas', 'tres provincias', 'infierno']
embalses = ['camporredondo', 'compuerto', 'requejada', 'ruesga']
rios = []
paises = ['Francia', 'España', 'Italia', 'Portugal']
ciudades = ['madrid', 'barcelona', 'bilbao', 'zaragoza', 'sevilla', 'valladolid', 'burgos', 'lugo', 'pontevedra', 'coruña', 'santiago', 'salamanca', 'zamora', 'avila']
idiomas = ['inglés', 'francés', 'español', 'portugues', 'ruso', 'alemán', 'griego', 'danés', 'noruego', 'sueco']

#Montañas
print(f'\tEsta es la lista inicial de MONTAÑAS: {montañas}')
print(f'Accedemos a los elementos con indice 0 y 5: {montañas[0]} y {montañas[5]}')
print(f'Mejoramos la presentación usando el método title(): {montañas[0].title()} y {montañas[5].title()}.')
print(f'Último elemento de la lista: {montañas[-1].title()}.')
message = f'Mi monte favorito de todos ellos es el Pico {montañas[5].title()}, con 2.525 msnm.'
print(message)

print(f'\n\tRecordamos la lista inicial: {montañas}.')
montañas[3] = 'tres mares'
print(f'Hemos modificado el elemento con indice 3 en la lista, ahora es {montañas[3].title()}.')
print(f'Esta es la lista ahora: {montañas}')
montañas.append('labra')
montañas.append('internauta')
montañas.append('tío celestino')
print(f'Con el método append añadimos varios nuevos montes a la lista. La lista: {montañas}.')
print(f'Con el método insert() añadimos nuevos elementos eligiendo su posición. Por ejemplo, añado el pico Cuartas en posición 2 (1), y seguido imprimo la lista.')
montañas.insert(1, 'cuartas')
print(montañas)
del montañas[1]
print(f'He eliminado el Pico Cuartas, muestro de nuevo la lista: {montañas}.')

#Embalses
print(f'\n\tLista inicial de embalses: {embalses}.')
popped_embalses = embalses.pop()
print(f'Hemos usado el método pop(). Elemento retirado: {popped_embalses}, lista actual: {embalses}.')
popped_embalses = embalses.pop(0)
print(f'Con pop() podemos especificar la posición que retiramos de la lista. Acabamos de retirar el elemento con indice 0, {popped_embalses}, lista actual: {embalses}.')

#Países
print(f'\n\tLista inicial de países: {paises}')
paises.remove('Francia')
print(f'Método remove(), borrando por contenido. Lista actual: {paises}')
too_far = 'Italia'
paises.remove(too_far)
print(f'Borrado a través de variable, listado actual: {paises}.')
print(f'{too_far} queda demasiado lejos.')

#Idiomas
print(f'\n\tListado inicial idiomas: {idiomas}.')
idiomas.sort()
print(f'Ordenados alf. y perm. Lista: {idiomas}.')
idiomas.sort(reverse=True)
print(f'Ordenados alf. inv. y perm. Lista: {idiomas}.')

#Ciudades
print(f'\n\tLista inical de ciudades: {ciudades}.')
print(f'Ord. temp.: {sorted(ciudades)}.')
print(f'Rescatamos la lista: {ciudades}.')
ciudades.reverse()
print(f'Hemos invertido de forma perm. el orden de la lista, con reverse; {ciudades}.')
print(f'Método len para conocer el número de ciudades guardadas en la lista: {len(ciudades)} ciudades.')
print(f'¿Cuál es la última ciudad de la lista? {ciudades[-1].title()}.')
#Ejercicio 311, forzando error de indice en una lista. print(f'{ciudades[14]}')