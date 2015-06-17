#!/usr/bin/env python

import pygal
from pygal.style import CleanStyle

### LAST 5
### select * from (SELECT * FROM sensordata ORDER BY date DESC LIMIT 5) ORDER BY date ASC;

### FIRST 5
### select * from sensordata ORDER BY date LIMIT 5;

### show how many rows:
### sqlite> select count(*), * from sensordata;
### 43|1434532393.07|28.1|63.5

#cvsFilesPath = '/home/pi/graphs/'
cvsFilesPath = '/tmp/' ### DEBUG

import sqlite3
conn = sqlite3.connect("thg.db")
curs = conn.cursor()

import datetime

def complete_data_graph():
  curs.execute("SELECT date FROM sensordata")
  timestamps = curs.fetchall()
  curs.execute("SELECT temp FROM sensordata")
  tempdata = curs.fetchall()
  curs.execute("SELECT humidity FROM sensordata")
  humdata = curs.fetchall()
  hdata = []
  tdata = []
  tstamps = []
  for i in humdata:
    hdata.append(float(i[0].encode("utf-8")))
  for j in tempdata:
    tdata.append(float(j[0].encode("utf-8")))
  for k in timestamps:
    tstamps.append(datetime.datetime.fromtimestamp(float(k[0].encode("utf-8"))).strftime('%Y-%m-%d %H:%M:%S'))
  #print hdata
  #print tdata
  #print tstamps

  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='every 30 minutes',x_labels_major_every=10,x_label_rotation=60, label_font_size=7, major_label_font_size=10)
  line_chart.title = 'Temperature & Humidity'
  line_chart.add('Temperature *C', tdata)
  line_chart.add('Humidity %', hdata, secondary=True) 
  line_chart.x_labels = tstamps
  line_chart.render_to_file('%s/temp-hum.svg' %cvsFilesPath)

def lastNhoursGraph(hours):
  hours = int(hours) * 2
  return



##   # last 48h graph
##   line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='Time in hours',x_labels_major_every=6,x_label_rotation=60)
##   line_chart.title = 'Temperature & Humidity last 48h'
##   line_chart.add('Temperature *C', last48_temp)
##   line_chart.add('Humidity %', last48_hum, secondary=True) 
##   line_chart.render_to_file('/home/pi/graphs/last48h-temp-hum.svg')
##   
##   # last 24h graph
##   line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='Time in hours',x_labels_major_every=6,x_label_rotation=60)
##   line_chart.title = 'Temperature & Humidity last 24h'
##   line_chart.add('Temperature *C', last24_temp)
##   line_chart.add('Humidity %', last24_hum, secondary=True) 
##   line_chart.render_to_file('/home/pi/graphs/last24h-temp-hum.svg')
## 
## create_graph(temp,hum)
complete_data_graph()
lastNhoursGraph(48) #hardcoded for tests

conn.close()
