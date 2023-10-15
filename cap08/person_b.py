#En las pruebas condicionales None se evalua como False
def build_person(first_name, last_name, age=None):
    """Devuelve un diccionario de información sobre una persona."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimmy', 'hendrix', 27)
print(musician)