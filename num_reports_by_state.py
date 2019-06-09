import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

import random
import operator

data = open('data.csv', 'r')

state_names = {
  'AK': 'Alaska',
  'AL': 'Alabama',
  'AR': 'Arkansas',
  'AS': 'American Samoa',
  'AZ': 'Arizona',
  'CA': 'California',
  'CO': 'Colorado',
  'CT': 'Connecticut',
  'DC': 'District of Columbia',
  'DE': 'Delaware',
  'FL': 'Florida',
  'GA': 'Georgia',
  'GU': 'Guam',
  'HI': 'Hawaii',
  'IA': 'Iowa',
  'ID': 'Idaho',
  'IL': 'Illinois',
  'IN': 'Indiana',
  'KS': 'Kansas',
  'KY': 'Kentucky',
  'LA': 'Louisiana',
  'MA': 'Massachusetts',
  'MD': 'Maryland',
  'ME': 'Maine',
  'MI': 'Michigan',
  'MN': 'Minnesota',
  'MO': 'Missouri',
  'MP': 'Northern Mariana Islands',
  'MS': 'Mississippi',
  'MT': 'Montana',
  'NA': 'National',
  'NC': 'North Carolina',
  'ND': 'North Dakota',
  'NE': 'Nebraska',
  'NH': 'New Hampshire',
  'NJ': 'New Jersey',
  'NM': 'New Mexico',
  'NV': 'Nevada',
  'NY': 'New York',
  'OH': 'Ohio',
  'OK': 'Oklahoma',
  'OR': 'Oregon',
  'PA': 'Pennsylvania',
  'PR': 'Puerto Rico',
  'RI': 'Rhode Island',
  'SC': 'South Carolina',
  'SD': 'South Dakota',
  'TN': 'Tennessee',
  'TX': 'Texas',
  'UT': 'Utah',
  'VA': 'Virginia',
  'VI': 'Virgin Islands',
  'VT': 'Vermont',
  'WA': 'Washington',
  'WI': 'Wisconsin',
  'WV': 'West Virginia',
  'WY': 'Wyoming',
  'AB': 'Alberta',
  'BC': 'British Columbia',
  'MB': 'Manitoba',
  'NB': 'New Brunswick',
  'NL': 'Newfoundland and Labrador',
  'NT': 'Northwest Territories',
  'NS': 'Nova Scotia',
  'NU': 'Nunavut',
  'ON': 'Ontario',
  'PE': 'Prince Edward Island',
  'QC': 'Quebec',
  'SK': 'Saskatchewan',
  'YT': 'Yukon'
}

states = {}
for line in data: 
  state = line.split(',')[4].rstrip().replace('"', "").replace(" ", "").upper()
  if state not in states.keys(): 
    states[state] = 1 
  else: 
    states[state] += 1 

states_cleaned = {}

for key in states.keys(): 
  if len(key) == 2 and key != "PQ" and key != "31" and key != "YK" and key != "SA" and key != "NF": 
    states_cleaned[state_names[key]] = states[key]


sorted_data = sorted(states_cleaned.items(), key=operator.itemgetter(1))[::-1][:-1]

layout = go.Layout(
  xaxis=dict(title='Province, State or Territory'),
  yaxis=dict(title='Total Number of Reports'),
  title = 'Number of UFO Sighting Reports by Region'
)

data = [go.Bar(
        x=np.array([x[0] for x in sorted_data]),
        y=np.array([x[1] for x in sorted_data])
       )]

plotly.offline.plot({'data': data, 'layout': layout}, filename='reports-by-state.html')


data = [go.Box(
        x=np.array([x[1] for x in sorted_data]),
       )]
layout = go.Layout(
  title = 'Number of UFO Sighting Reports by Region'
)

plotly.offline.plot({'data': data, 'layout': layout}, filename='reports-by-state-box.html')

print(states_cleaned)
print(len(sorted_data))