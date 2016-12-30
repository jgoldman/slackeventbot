import os
import subprocess 
import time
from slackclient import SlackClient


# slack_token = 'xoxp-6354740753-101554727523-121009606037-535cfd995d88810d73cf1a3283ae9a84'
slack_token = 'xoxp-120041460657-120720635442-120652984483-ebf82c75b08c59633355a55bb9b03747'
sc = SlackClient(slack_token)

wdir = './scrapers/'
for scraper in os.listdir(wdir):
	new_events = subprocess.call(["python", wdir + scraper])
	print(new_events)
	for key, value in new_events.items():
		domain = key.split('/')[0]
		print('key')
		print(key)
		# sc.api_call(
		#   "chat.postMessage",
		#   # channel="#sf_events",
		#   channel="#general",
		#   username="eventGuide",
		#   text='<' + key +'| Top Events of ' + domain + ' for ' + time.strftime('%m/%d') + ':>\n>>>' + '\n'.join(value)
		# )
