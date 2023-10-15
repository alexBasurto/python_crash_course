edad_persona = 200

if edad_persona < 2:
    etapa = 'bebé'
elif edad_persona < 4:
    etapa = 'infante'
elif edad_persona < 13:
    etapa = 'niño'
elif edad_persona < 20:
    etapa = 'adolescente'
elif edad_persona < 65:
    etapa = 'adulto'
elif edad_persona < 200:
    etapa = 'jubilado'
elif edad_persona >= 200:
    etapa = 'cyborg'

print(f"Esta persona, con {edad_persona} años es un {etapa}.")