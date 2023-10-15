holidays = {}

holiday_poll = True

while holiday_poll:
    prompt1 = "\n¿Cómo te llamas? "
    name = input(prompt1)
    prompt2 = "Si pudieras visitar cualquier lugar del mundo, ¿dónde irías? "
    destiny = input(prompt2)
    holidays[name] = destiny
    repeat = input("¿Alguien más que quiera contestar? (si/no)")
    if repeat == 'no':
        holiday_poll = False

for name, destiny in holidays.items():
    print(f"\t - ¡Las vacaciones favoritas de {name.title()} serían en {destiny.title()}!")