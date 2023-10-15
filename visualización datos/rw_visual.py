import matplotlib.pyplot as plt

from random_walk_bckup import Randomwalk

#Sigue generando caminos nuevos mientras el programa esté activo.
while True:
    # Hace un camino aleatorio
    rw = Randomwalk(50_000)
    rw.fill_walk()

    #Traza los puntos del camino
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20,12))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Enfatiza el primer punto y el último
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Elimina los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #plt.savefig('camino_aleatorio.png')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break