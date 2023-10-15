numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    if numero == 1:
        sufijo = "st"
    elif numero == 2:
        sufijo = "nd"
    elif numero == 3:
        sufijo = "rd"
    else:
        sufijo = "th"
    print(f"\n{numero}{sufijo}")