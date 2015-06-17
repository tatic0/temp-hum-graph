#!/usr/bin/env python

import pygal
from pygal.style import CleanStyle

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

  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='every 30 minutes',x_labels_major_every=10,x_label_rotation=60, label_font_size=7, major_label_font_size=10)
  line_chart.title = 'Temperature & Humidity'
  line_chart.add('Temperature *C', tdata)
  line_chart.add('Humidity %', hdata, secondary=True) 
  line_chart.x_labels = tstamps
  line_chart.render_to_file('%s/temp-hum.svg' %cvsFilesPath)

def lastNhoursGraph(hours):
  hours2 = int(hours) * 2
  curs.execute("SELECT * FROM (SELECT date FROM sensordata ORDER BY date DESC LIMIT ?) ORDER BY date ASC", (hours2,))
  timestamps = curs.fetchall()
  curs.execute('SELECT temp FROM (SELECT temp, date FROM sensordata ORDER BY date DESC LIMIT ?) ORDER BY date ASC', (hours2,))
  tempdata = curs.fetchall()
  curs.execute('SELECT humidity FROM (SELECT humidity, date FROM sensordata ORDER BY date DESC LIMIT ?) ORDER BY date ASC', (hours2,))
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

  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='every 30 minutes',x_labels_major_every=10,x_label_rotation=60, label_font_size=7, major_label_font_size=10)
  line_chart.title = 'Temperature & Humidity'
  line_chart.add('Temperature *C', tdata)
  line_chart.add('Humidity %', hdata, secondary=True) 
  line_chart.x_labels = tstamps
  line_chart.render_to_file('%s/last-%s-temp-hum.svg' %(cvsFilesPath,hours))


complete_data_graph()
for i in [ 12, 24, 48, 96]:
  lastNhoursGraph(i) #hardcoded for tests

conn.close()
