from bs4 import BeautifulSoup
import time
import sys
import json
import requests

def get_html(link):
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
       return get_html(link)

def main():
  """
   Grab the html source for a link, return it as a string.
  """        

  html = get_html('http://sf.funcheap.com/category/event/top-pick/')
  soupHTML = BeautifulSoup(html, 'lxml')
  elements = soupHTML.find(attrs={'id': 'content'}).find(attrs={'class': 'clearfloat'}).find_all('div')

  current_el = None
  events = {}

  months = {'01': 'january','02': 'february','03': 'march','04': 'april','05': 'may','06': 'june','07': 'july','08': 'august','09': 'september','10': 'october','11': 'november','12': 'december'}
  current_day =  time.strftime('%d')

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
  print(json.dumps({'http://sf.funcheap.com/category/event/top-pick/': events[current_day]}))

if __name__ == "__main__":
  main()