import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import csv
from datetime import datetime

# Explora la estructura de los datos.
filename = 'data/world_fires_1_day.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    ixLat = header_row.index('latitude')
    ixLon = header_row.index('longitude')
    ixBri = header_row.index('brightness')
    ixAcqDate = header_row.index('acq_date')
    ixDayNight = header_row.index('daynight')

    lats, lons, bris, dates, daynights = [], [], [], [], []
    for row in reader:
        lats.append(row[ixLat])
        lons.append(row[ixLon])
        bris.append(float(row[ixBri]))
        dates.append(row[ixAcqDate])
        daynights.append(row[ixDayNight])

# Mapea los incendios.
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker': {
        'size': [0.05*bri for bri in bris],
        'color': bris,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
    }]
my_layout = Layout(title="World fires 1 day")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')