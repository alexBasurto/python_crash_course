def get_formatted_name(first_name, last_name, middle_name=''):
    """Devuelve un nombre completo, con un formato adecuado."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


musician = get_formatted_name('jimmy', 'hendrix')
print(musician)