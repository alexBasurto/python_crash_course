invitados = ['john f. kennedy', 'bill gates', 'steve jobs']
print(f'\n\tQuerido {invitados[0].title()}, a mi mujer y a mí nos gustaría invitarle a cenar a nuestra casa.')
print(f'\n\tQuerido {invitados[1].title()}, a mi mujer y a mí nos gustaría invitarle a cenar a nuestra casa.')
print(f'\n\tQuerido {invitados[2].title()}, a mi mujer y a mí nos gustaría invitarle a cenar a nuestra casa.')

print(f"\n\t\tUno de nuestros invitados no podrá asistir, se trata de {invitados[0].title()}, tuvo un problemilla en Dallas.")

invitados[0] = "barack obama"
print(f'\n\tQuerido {invitados[0].title()}, a mi mujer y a mí nos gustaría invitarle a cenar a nuestra casa.')
print(f'\n\tQuerido {invitados[1].title()}, a mi mujer y a mí nos gustaría invitarle a cenar a nuestra casa.')
print(f'\n\tQuerido {invitados[2].title()}, a mi mujer y a mí nos gustaría invitarle a cenar a nuestra casa.')

print(f"\n\t\tAl final parece que tenemos una mesa para 8 comensales. Podemos invitar a 3 personas más.")
invitados.insert(0, 'michael jordan')
invitados.insert(2, 'michael phelps')
invitados.append('freddy mercury')
print(f'\n\tQuerido {invitados[0].title()}, le escribo para informarle de que al final seremos 8 personas a la mesa, al haber encontrado una mesa más grande donde cenar')
print(f'\n\tQuerido {invitados[1].title()}, le escribo para informarle de que al final seremos 8 personas a la mesa, al haber encontrado una mesa más grande donde cenar')
print(f'\n\tQuerido {invitados[2].title()}, le escribo para informarle de que al final seremos 8 personas a la mesa, al haber encontrado una mesa más grande donde cenar')
print(f'\n\tQuerido {invitados[3].title()}, le escribo para informarle de que al final seremos 8 personas a la mesa, al haber encontrado una mesa más grande donde cenar')
print(f'\n\tQuerido {invitados[4].title()}, le escribo para informarle de que al final seremos 8 personas a la mesa, al haber encontrado una mesa más grande donde cenar')
print(f'\n\tQuerido {invitados[5].title()}, le escribo para informarle de que al final seremos 8 personas a la mesa, al haber encontrado una mesa más grande donde cenar')

print("\n\t\t¡Vaya cagada! Al final la mesa no va a llegar, por lo que solo tenemos sitio para 2 invitados")
invitado_rechazado = invitados.pop()
print(f"\n\tLo sentimos mucho, {invitado_rechazado.title()}, pero se ha cancelado la cena. Nos veremos en otra ocasión.")
invitado_rechazado = invitados.pop()
print(f"\n\tLo sentimos mucho, {invitado_rechazado.title()}, pero se ha cancelado la cena. Nos veremos en otra ocasión.")
invitado_rechazado = invitados.pop()
print(f"\n\tLo sentimos mucho, {invitado_rechazado.title()}, pero se ha cancelado la cena. Nos veremos en otra ocasión.")
invitado_rechazado = invitados.pop()
print(f"\n\tLo sentimos mucho, {invitado_rechazado.title()}, pero se ha cancelado la cena. Nos veremos en otra ocasión.")

print('\n\t\tRecordamos a los dos invitados finales que siguen invitados a la cena:')
print(f'\n\tSr. {invitados[0].title()}, le recordamos que sigue invitado a la cena.')
print(f'\n\tSr. {invitados[1].title()}, le recordamos que sigue invitado a la cena.')

#ejercicio 39

print(f'El número de personas invitadas finalmente a la cena es de {len(invitados)}.')