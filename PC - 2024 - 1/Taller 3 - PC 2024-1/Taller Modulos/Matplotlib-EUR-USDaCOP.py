'''Punto 2. Taller Modulos, Presentado por:
Nicolas Fuentes Ramos
Santiago Cardenas Rodriguez
Juan Jose Roldan'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv

#Recoleccion de datos
USDEx = []
EUREx = []
with open('USDaCOP.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in rowreader:
        USDEx.append(float(row[1].replace(",", "")))
        
with open('EURaCOP.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in rowreader:
        EUREx.append(float(row[1].replace(",", "")))

#Establecer el periodo de tiempo
start = pd.Timestamp(2023, 1, 1, 12)
end = pd.Timestamp(2023, 8, 31, 12, 0, 0)
times = pd.date_range(freq='1d', start=start, end=end)

#Crear los dataframes con la informacion anterior
df = pd.DataFrame(data={'USD_a_COP': USDEx, 'EUR_a_COP': EUREx}, index=times)

#Creacion y configuracion de las graficas
fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(df['USD_a_COP'], 'k', label='USD a COP')
ax.plot(df['EUR_a_COP'], 'r', label='EUR a COP')
ax.set_xlabel('Fecha')
ax.set_ylabel('Tipo de Cambio a COP')
ax.set_title('Tipo de Cambio USD y EUR a COP (Enero - Agosto 2023)')  # Agregar título
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
fig.autofmt_xdate(rotation=45)
ax.legend()
plt.show()