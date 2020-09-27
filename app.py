import os
import time
import requests
import json

url = 'http://0.0.0.0:5000/pi_temps'

def measure_temp():
	# temp = os.popen("vcgencmd measure_temp").readline()
	temp=35.0
	data={'temp':35.0}
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	# r = requests.post(url, data=data)
	# r = requests.post(url, data=json.dumps(data))
	r = requests.post(url, data=data, headers=headers)
	print(r.status_code)
	print(r.reason)

while True:
	print(measure_temp())
	time.sleep(10)