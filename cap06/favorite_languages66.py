favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'alex': 'python',
    }

language_sarah = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language_sarah}.\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\nRellenaron la encuesta:")
for name in favorite_languages.keys(): #keys() es el método predeterminado, por lo que la coletilla .keys() podría obviarse
    print(name.title())

print("\nEstas son las respuestas:")
for language in favorite_languages.values():
    print(language.title())

print("\n\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

print("\n\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n\n")

if 'c#' not in favorite_languages.values():
    print("C# hasn't been choosen by anybody.")

print("\n\n")

for name in sorted(favorite_languages.keys()): #ordenado alfabéticamente. En este caso sorted es una función.
    print(f"{name.title()}, thank you for taking the poll!")

print("\n\n")

#este código está creado por mi, para mostrar solo una vez cada lenguaje.
languages = []
for language in favorite_languages.values():  
    if language not in languages:
        print(language)
    languages.append(language)

#pero en el libro aparece una forma mejor, utilizando un conjunto:
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language)

pendientes = ['carlos', 'jen', 'sarah', 'pedro', 'marimar', 'edward', 'aitor', 'rosa']
for pendiente in pendientes:
    if pendiente in favorite_languages.keys():
        print(f"Gracias {pendiente.title()}, usted ya rellenó la encuesta.")
    else:
        print(f"Sr./Sra. {pendiente.title()}, rellene la encuesta, por favor.")