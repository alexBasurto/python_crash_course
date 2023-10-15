#Emplear bucles while con listas y diccionarios nos permite recoger, almacenar y organizar
#muchas entradas para examinarlas e informar luego.

#empieza con usuarios que hay que verificar,
#y una lista vacía para alojar a los usuarios confirmados.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
import time

#Verifica cada usuario hasta que ya no hay usuarios sin confirmar.
#Mueve a cada usuario verificado a la lista de usuarios confirmados.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".")

    confirmed_users.append(current_user)

#Muestra todos los usuarios confirmados.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())