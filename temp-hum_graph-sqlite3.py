#!/usr/bin/env python

import pygal
from pygal.style import CleanStyle

### this returns tuples:
### >>> import sqlite3
### >>> conn = sqlite3.connect("thg.db")
### >>> curs = conn.cursor()
### >>> curs.execute("SELECT * FROM sensordata")
### <sqlite3.Cursor object at 0x7fb34d975a40>
### >>> data = curs.fetchall()
### >>> print(data)
### [(u'1434363109.8', u'24.1', u'50.0'), (u'1434379412.23', u'24.1', u'50.0'), (u'1434379444.44', u'24.1', u'50.0'), (u'
### 1434379467.58', u'24.1', u'50.0')]
### >>> for i in data:
### ...     print i
### ...     
### ... 
### (u'1434363109.8', u'24.1', u'50.0')
### (u'1434379412.23', u'24.1', u'50.0')
### (u'1434379444.44', u'24.1', u'50.0')
### (u'1434379467.58', u'24.1', u'50.0')

### LAST 5
### select * from (SELECT * FROM sensordata ORDER BY date DESC LIMIT 5) ORDER BY date ASC;

### FIRST 5
### select * from sensordata ORDER BY date LIMIT 5;

### show how many rows:
### sqlite> select count(*), * from sensordata;
### 43|1434532393.07|28.1|63.5

temp = []
hum  = []

#cvsFilesPath = '/home/pi/graphs/'
cvsFilesPath = '/tmp/' ### DEBUG

# x_range = ['1',]
# x_counter = 0
# counter = 0
# logdata = open('/home/pi/temp-hum.log','r')
# for line in logdata.readlines():
#   line = line.split()[1:]
#   temp.append(float(line[0]))
#   hum.append(float(line[1]))
#   counter +=1
#   x_counter +=.5
#   x_range.append(str(x_counter))


# print("temperature: \n %s") %str(temp)
# print("humidity: \n %s") % str(hum)
# print("counter %d") % counter
# print(x_range)

import sqlite3
conn = sqlite3.connect("thg.db")
curs = conn.cursor()

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
    tstamps.append(k[0].encode("utf-8"))
  #print hdata
  #print tdata
  #print tstamps

  line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='every 30 minutes',x_labels_major_every=6,x_label_rotation=60)
  line_chart.title = 'Temperature & Humidity'
  line_chart.add('Temperature *C', tdata)
  line_chart.add('Humidity %', hdata, secondary=True) 
  line_chart.render_to_file('%s/temp-hum.svg' %cvsFilesPath)

## def create_graph(tdata,hdata):
##   ## better get all data at once and do the [-xx:] here?
##   ## split in different functions?
##   ## limit max size for log file? (like [-1000:]
##   
##   last24_temp = tdata[-48:]
##   last24_hum = hdata[-48:]
##   last48_temp = tdata[-96:]
##   last48_hum = hdata[-96:]
##   # all data graph
##   line_chart = pygal.Line(style=CleanStyle, width=1200,order_min=-1,x_title='Time in hours',x_labels_major_every=6,x_label_rotation=60)
##   line_chart.title = 'Temperature & Humidity'
##   line_chart.add('Temperature *C', tdata)
##   line_chart.add('Humidity %', hdata, secondary=True) 
##   line_chart.render_to_file('/home/pi/graphs/temp-hum.svg')
##   
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
