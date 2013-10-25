#!/usr/bin/env python

import pygal
from pygal.style import CleanStyle

temp = []
hum  = []

x_range = ['1',]
x_counter = 0
counter = 0
logdata = open('/home/pi/temp-hum.log','r')
for line in logdata.readlines():
  line = line.split()[1:]
  temp.append(float(line[0]))
  hum.append(float(line[1]))
  counter +=1
  x_counter +=.5
  x_range.append(str(x_counter))


print("temperature: \n %s") %str(temp)
print("humidity: \n %s") % str(hum)
print("counter %d") % counter
print(x_range)


def create_graph(tdata,hdata):
  ## better get all data at once and do the [-xx:] here?
  ## split in different functions?
  ## limit max size for log file? (like [-1000:]
  
  last24_temp = tdata[-48:]
  last24_hum = hdata[-48:]
  last48_temp = tdata[-96:]
  last48_hum = hdata[-96:]
  # all data graph
  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='Time in hours',x_labels_major_every=6,x_label_rotation=60)
  line_chart.title = 'Temperature & Humidity'
  line_chart.add('Temperature *C', tdata)
  line_chart.add('Humidity %', hdata, secondary=True) 
  line_chart.render_to_file('/home/pi/graphs/temp-hum.svg')
  
  # last 48h graph
  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='Time in hours',x_labels_major_every=6,x_label_rotation=60)
  line_chart.title = 'Temperature & Humidity last 48h'
  line_chart.add('Temperature *C', last48_temp)
  line_chart.add('Humidity %', last48_hum, secondary=True) 
  line_chart.render_to_file('/home/pi/graphs/last48h-temp-hum.svg')
  
  # last 24h graph
  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='Time in hours',x_labels_major_every=6,x_label_rotation=60)
  line_chart.title = 'Temperature & Humidity last 24h'
  line_chart.add('Temperature *C', last24_temp)
  line_chart.add('Humidity %', last24_hum, secondary=True) 
  line_chart.render_to_file('/home/pi/graphs/last24h-temp-hum.svg')

create_graph(temp,hum)
