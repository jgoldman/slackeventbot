import os
import subprocess 
import time
import requests

wdir = './scrapers/'
for scraper in os.listdir(wdir):
	new_events = subprocess.call(["python", wdir + scraper])
	print(new_events)
	for key, value in new_events.items():
		domain = key.split('/')[0]
		print(key)
		# sc.api_call(
		#   "chat.postMessage",
		#   # channel="#sf_events",
		#   channel="#general",
		#   username="eventGuide",
		#   text='<' + key +'| Top Events of ' + domain + ' for ' + time.strftime('%m/%d') + ':>\n>>>' + '\n'.join(value)
		# )
