import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pyperclip
import numpy as np
from scipy import stats
import random
import operator

data = open('data.csv', 'r')

things = 0 
years = {}
for line in data: 
  try: 
    year = int(line.split(',')[1].split("/")[2].split()[0])
  except: 
    continue
  if year < 1995 or year == 2019: 
    continue
  if year in years.keys(): 
    years[year] += 1 
  else: 
    years[year] = 1
  things += 1 



sorted_data = []
print(things)
for year in range(1995, 2019):
  sorted_data.append([year, years[year]])

# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(np.array([x[0] for x in sorted_data]),np.array([x[1] for x in sorted_data]))
line = slope*np.array([x[0] for x in sorted_data])+intercept
print(slope, intercept, r_value)
LINE = go.Scatter(
                  x=np.array([x[0] for x in sorted_data]),
                  y=line,
                  mode='lines',
                  marker=go.Marker(color='rgb(180, 0, 0)'),
                  name='Fit'
                  )


layout = go.Layout(
  xaxis=dict(title='Year'),
  yaxis=dict(title='Number of UFO Sightings'),
  title = 'Year vs. Number of UFO Sighting Reports'
)


data = [go.Bar(
        y=np.array([x[1] for x in sorted_data]),
        x=np.array([x[0] for x in sorted_data]),
       ), LINE]

# layout = go.Layout(
#   title = 'Average Number of UFO Sightings from 2000 to 2018'
# )

plotly.offline.plot({'data': data, 'layout': layout}, filename='reports-by-year.html')
