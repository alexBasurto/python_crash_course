def build_person(first_name, last_name):
    """Devuelve un diccionario de información sobre una persona."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimmy', 'hendrix')
print(musician)