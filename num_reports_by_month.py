import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from scipy import stats
import random
import operator

data = open('data.csv', 'r')
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

months = {}

things = 0 
for line in data: 
  try: 
    line.split(',')[1].split("/")[1]
    year = int(line.split(',')[1].split("/")[2].split()[0])
    month = month_names[(int(line.split(',')[1].split("/")[0])) - 1]
  except: 
    continue
  if year < 2000 or year == 2019: 
    continue
  if month not in months.keys(): 
    months[month] = 1 
  else: 
    months[month] += 1 
  things += 1 

sorted_data = sorted(months.items())

layout = go.Layout(
  xaxis=dict(title='Month'),
  yaxis=dict(title='Total Number of Reports per Month'),
  title = 'Months vs. Number of UFO Sighting Reports'
)


data = [go.Bar(
        y=np.array([x[1] for x in sorted_data]),
        x=np.array([x[0] for x in sorted_data]),
       )]
layout = go.Layout(
  title = 'Average Number of UFO Sightings from 2000 to 2018'
)

plotly.offline.plot({'data': data, 'layout': layout}, filename='reports-by-month.html')
print(np.std(np.array(sorted_data)))
zscores = (list(abs(x) for x in stats.zscore(np.array(sorted_data))))
print(sum(zscores) / 12)
