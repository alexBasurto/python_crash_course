lugares_favoritos = {
    'lidia': ['salinas', 'hervás', 'basauri'],
    'arturo': ['castro urdiales', 'cambrils', 'riocavado'],
    'mario': ['cervera de pisuerga', 'aguilar de campoo', 'salinas de pisuerga'],
    'idoia': ['santillana del mar'],
    'martina': ['casa de amama', 'parque'],
    }

for persona, lugares in lugares_favoritos.items():
    if len(lugares) == 1:
        print(f"\nEl lugar favorito de {persona.title()} es {lugares[0].title()}")
    else:
        print(f"\nLos lugares favoritos de {persona.title()} son:")
        for lugar in lugares:
            print(f"\t{lugar.title()}")
