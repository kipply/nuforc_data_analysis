import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from scipy import stats
import numpy as np
import pyperclip

import random
import operator

data = open('cleaned_data.csv', 'r')
data_x = []
data_y = []

for line in data: 
  if float(line.split(',')[4]) < 0 or float(line.split(',')[4]) > 300: 
    continue
  data_x.append(float(line.split(',')[4]))
  data_y.append(len(line.split(',')[5].split()))
    
layout = go.Layout(
    xaxis = go.layout.XAxis(
      title="Duration in Seconds"
    ),
  yaxis=dict(title='Words in Report'),
  title = 'Sighting Duration vs Words in Report'
)

data = [go.Scatter(
  x=np.array(data_x),
  y=np.array(data_y),
  mode = 'markers'
       )]


plotly.offline.plot({'data': data, 'layout': layout}, filename='duration-word-count.html')

pyperclip.copy("\n".join(map(str, data_y)))
