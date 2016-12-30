print(__name__)
import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient
import time

# slack_token = 'xoxp-6354740753-101554727523-121009606037-535cfd995d88810d73cf1a3283ae9a84'
slack_token = 'xoxp-120041460657-120720635442-120652984483-ebf82c75b08c59633355a55bb9b03747'
sc = SlackClient(slack_token)

def grab_html_source(link):
   """
   Grab the html source for a link, return it as a string.
   """        

   session = requests.Session()
   session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
   r = session.get(link)
   
   if r.ok:
       return r.content
   else:
       print("ERROR: " + link)
       return grab_html_source(link)

def __main__():
	html = grab_html_source('http://sf.funcheap.com/category/event/top-pick/')
	soupHTML = BeautifulSoup(html, 'lxml')
	# days = soupHTML.find_all(attrs={'class': 'archive_date_title'})

	elements = soupHTML.find(attrs={'id': 'content'}).find(attrs={'class': 'clearfloat'}).find_all('div')

	current_el = None
	events = {}

	for e in elements:
		try:
			class_string = ''.join(e['class'])
			if class_string == 'archive_date_title':
				current_el = e.text.split(', ')[1].lower().split(' ')[1]
				events[current_el] = []
			else:
				event_detail = e.find(attrs={'class': 'title'}).find('a')
				text = '<'+event_detail['href'] + '|' + event_detail.text+'>'
				events[current_el].append(text.encode('utf-8'))
		except:
			pass
	months = {'01': 'january','02': 'february','03': 'march','04': 'april','05': 'may','06': 'june','07': 'july','08': 'august','09': 'september','10': 'october','11': 'november','12': 'december'}
	# day_list = [d.text.split(', ')[1].lower().split(' ') for d in days]
	print('test 123')
	current_day =  time.strftime('%d')
	# current_day = current_day.split('/')
	return {'http://sf.funcheap.com/category/event/top-pick/': events[current_day]}

	# if __name__ == '__main__':
 #    hello()