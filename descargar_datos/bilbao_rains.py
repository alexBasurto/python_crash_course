import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Obtiene fechas y precipitaciones de este archivo
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(rain)

# Traza las lluvias
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue', alpha=0.5)
plt.fill_between(dates, rains, 0, facecolor='blue', alpha=0.1)

# Da formato al trazado
title = "Daily rains - 2018\Bilbao Aeropuerto - SP"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rains (tenths of mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()