#!/usr/bin/env python

import os
import sys

""" This script creates and initializes the database """

try:
  import sqlite3
except ImportError:
  print("Please install sqlite3 for python")
  print("you can use 'pip install sqlite3' or use your preferred package manager")

if os.path.isfile('thg.db'):
  print('database already created')
  sys.exit(0)
else:
  conn = sqlite3.connect("thg.db")
  curs = conn.cursor()
  curs.execute('CREATE TABLE sensordata ( date text, temp text, humidity text )')
  print("database created!\nRunning some tests")
  conn.commit()
  curs.execute("INSERT INTO sensordata VALUES ('1434363109.8', '24.1', '50.0')")
  conn.commit()
  print("all good as far as now")
  curs.execute("SELECT * FROM sensordata")
  print(curs.fetchall())
  conn.commit()
  conn.close()
  print("database installed\nyou can now start to log the DHT data :)")
