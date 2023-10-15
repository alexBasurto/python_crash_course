#definimos la función
def greet_user_name(username): #username es un parametro de la función greeter_user_name
    """Muestra un simple saludo personalizado."""
    print(f"Hello, {username.title()}!")


#llamamos a la función
greet_user_name('alex') #alex es el argumento que pasamos para dar valor al parametro username
greet_user_name('lylo')

#a menudo la gente suele mezclar los términos PARAMETRO y ARGUMENTO
