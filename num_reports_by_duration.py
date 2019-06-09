import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from scipy import stats
import numpy as np

import random
import operator

data = open('cleaned_data.csv', 'r')
durations = []

data_points_over_one_day = 0 
for line in data: 
  if float(line.split(',')[4]) > 3750: 
    data_points_over_one_day += 1
    continue
  if float(line.split(',')[4]) < 0: 
    continue
  durations.append(float(line.split(',')[4]))


print(min(durations))
print(data_points_over_one_day)
    
# layout = go.Layout(
#     xaxis = go.layout.XAxis(
#       title="Duration",
#       tickmode = 'array',
#       tickvals = [250, 750, 1250, 1750, 2250, 2750, 3250, 3750],
#       ticktext = ['4 Minutes', '12 Minutes', '20 Minutes', '29 Minutes', '37 Minutes', '46 Minutes', '54 Minutes', '63 Minutes'],
#       range = [10, 3600]
#     ),
#   yaxis=dict(title='Number of Reports'),
#   title = 'Histogram of Sighting Durations'
# )

# data = [go.Histogram(
#         x=np.array(durations),
#         nbinsx = 10
#        )]

layout = go.Layout(
    xaxis = go.layout.XAxis(
      title="Duration",
      tickmode = 'array',
    ),
  yaxis=dict(title='Number of Reports'),
  title = 'Histogram of Sighting Durations'
)

data = [go.Box(
        x=np.array(durations),
        nbinsx = 10
       )]


plotly.offline.plot({'data': data, 'layout': layout}, filename='reports-by-duration-box.html')

print(np.std(np.array(durations)))
print(np.mean(stats.zscore(np.array(durations))))