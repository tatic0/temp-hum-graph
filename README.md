temp-hum-graph
==============

temperature &amp; humidity graph with pygal for raspberry pi + DHT22

dependencies:
-------------
* DHT driver by Adafruit:
 https://github.com/tatic0/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_DHT_Driver
* pygal
 pip install pygal

examples:
---------

crontab
 @reboot /usr/bin/sudo /home/pi/Adafruit_DHT_sqlite3.py
 */30 * * * * /usr/bin/python /home/pi/temp-hum_graph-sqlite3.py

