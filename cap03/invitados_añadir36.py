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