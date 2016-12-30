import os
import subprocess 
import time
from slackclient import SlackClient
import sys
import json

def main():
	"""
    Per scraper in ./scrapers send a message to slack
    """ 
	# from scrapers import *

	slack_token = 'xoxp-6354740753-101554727523-121009606037-535cfd995d88810d73cf1a3283ae9a84'
	# slack_token = 'xoxp-120041460657-120720635442-120652984483-ebf82c75b08c59633355a55bb9b03747'
	sc = SlackClient(slack_token)

	wdir = './scrapers/'
	for scraper in os.listdir(wdir):
		event_json = subprocess.check_output(['python', wdir + scraper])
		event_string = json.loads(event_json)
		for key, value in event_string.items():
			domain = key.split('/')[2]
			sc.api_call(
			  "chat.postMessage",
			  # channel="#sf_events",
			  channel="#sf_events",
			  username="eventGuide",
			  text='<' + key +'| Top Events of ' + domain + ' for ' + time.strftime('%m/%d') + ':>\n>>>' + '\n'.join(value)
			)
if __name__ == "__main__":
  main()