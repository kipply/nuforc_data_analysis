import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pyperclip
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

state_pops = [
  ["Texas",25145561  ],
  ["Florida",18801310  ],
  ["New York",19378102  ],
  ["Pennsylvania",12702379  ],
  ["Illinois",12830632  ],
  ["Ohio",11536504  ],
  ["Georgia",9687653  ],
  ["North Carolina",9535483  ],
  ["Michigan",9883640  ],
  ["New Jersey",8791894  ],
  ["Virginia",8001024  ],
  ["Washington",6724540  ],
  ["Arizona",6392017  ],
  ["Massachusetts",6547629  ],
  ["Tennessee",6346105  ],
  ["Indiana",6483802  ],
  ["Missouri",5988927  ],
  ["Maryland",5773552  ],
  ["Wisconsin",5686986  ],
  ["Colorado",5029196  ],
  ["Minnesota",5303925  ],
  ["South Carolina",4625364  ],
  ["Alabama",4779736  ],
  ["Louisiana",4533372  ],
  ["Kentucky",4339367  ],
  ["Oregon",3831074  ],
  ["Oklahoma",3751351  ],
  ["Connecticut",3574097  ],
  ["Puerto Rico",3725789  ],
  ["Utah",2763885  ],
  ["Iowa",3046355  ],
  ["Nevada",2700551  ],
  ["Arkansas",2915918  ],
  ["Mississippi",2967297  ],
  ["Kansas",2853118  ],
  ["New Mexico",2059179  ],
  ["Nebraska",1826341  ],
  ["West Virginia",1852994  ],
  ["Idaho",1567582  ],
  ["Hawaii",1360301  ],
  ["New Hampshire",1316470  ],
  ["Maine",1328361  ],
  ["Montana",989415  ],
  ["Rhode Island",1052567  ],
  ["Delaware",897934  ],
  ["South Dakota",814180  ],
  ["North Dakota",672591  ],
  ["Alaska",710231  ],
  ["District of Columbia",601723  ],
  ["Vermont",625741  ],
  ["Wyoming",563626  ]
]

state_eds = [
["Massachusetts",74.16  ],
["New Jersey",67.09  ],
  ["Connecticut",66.93  ],
  ["New Hampshire",65.11  ],
  ["Vermont",63.18  ],
  ["Virginia",63.03  ],
  ["Minnesota",60.34  ],
  ["Maryland",57.82  ],
  ["Wisconsin",57.59  ],
  ["Colorado",57.45  ],
  ["North Dakota",57.03  ],
  ["Wyoming",57.02  ],
  ["Maine",56.82  ],
  ["Nebraska",56.42  ],
  ["Kansas",55.55  ],
  ["Iowa",55.33  ],
  ["Rhode Island",54.78  ],
  ["Washington",54.58  ],
  ["Delaware",54.36  ],
  ["Kentucky",54.34  ],
  ["Illinois",54.2  ],
  ["New York",53.36  ],
  ["Montana",52.78  ],
  ["Indiana",52.69  ],
  ["South Dakota",52.27  ],
  ["Florida",52.1  ],
  ["Ohio",51.93  ],
  ["Pennsylvania",51.36  ],
  ["Missouri",51.2  ],
  ["Utah",50.99  ],
  ["Michigan",50.07  ],
  ["North Carolina",48.91  ],
  ["Oklahoma",48.79  ],
  ["Idaho",47.84  ],
  ["Tennessee",46.9  ],
  ["Texas",46.9  ],
  ["California",46.33  ],
  ["Georgia",45.67  ],
  ["Hawaii",45.09  ],
  ["South Carolina",42.24  ],
  ["Arkansas",42.18  ],
  ["West Virginia",39.91  ],
  ["Oregon",39.79  ],
  ["Alabama",38.98  ],
  ["Mississippi",38.87  ],
  ["Nevada",38.54  ],
  ["Arizona",37.53  ],
  ["Alaska",35.87  ],
  ["District of Columbia",33.62  ],
  ["Louisiana",32.5  ],
  ["New Mexico",31.53  ]
]
def get_state_pop(name): 
  for i in range(50): 
    if state_pops[i][0] == name: 
      return state_pops[i][1]
  return False 

def get_state_ed(name): 
  for i in range(51): 
    if state_eds[i][0] == name: 
      return state_eds[i][1]
  return False 


states = {}
for line in data: 
  state = line.split(',')[4].rstrip().replace('"', "").replace(" ", "").upper()
  if state not in states.keys(): 
    states[state] = 1 
  else: 
    states[state] += 1 

states_cleaned = {}
data_x = []
data_y = [] 

for key in states.keys(): 
  if len(key) == 2 and key != "PQ" and key != "PR" and key != "31" and key != "YK" and key != "SA" and key != "NF": 
    if (get_state_pop(state_names[key])): 
      states_cleaned[state_names[key]] = states[key] / get_state_pop(state_names[key])
      data_x.append(states[key] / get_state_pop(state_names[key]))
      data_y.append(get_state_ed(state_names[key]))
      if not get_state_ed(state_names[key]): 
        print(state_names[key])
sorted_data = sorted(states_cleaned.items(), key=operator.itemgetter(1))[::-1][:-1]

layout = go.Layout(
  xaxis=dict(title='UFO Reports per capita'),
  yaxis=dict(title='Education quality score'),
  title = 'Number of UFO Sightings vs Quality of Education'
)

# data = [go.Bar(
#         x=np.array([x[0] for x in sorted_data]),
#         y=np.array([x[1] for x in sorted_data])
#        )]


data = [go.Scatter(
  x=np.array(data_x),
  y=np.array(data_y),
  mode = 'markers'
       )]

for i in range(49): 
  print(data_x[i], data_y[i])

pyperclip.copy("\n".join(map(str, data_y)))
plotly.offline.plot({'data': data, 'layout': layout}, filename='reports-by-state-education.html')
