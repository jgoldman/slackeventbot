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

  current_day =  time.strftime('%d')

  for e in elements:
    try:
      class_string = ''.join(e['class'])
      if class_string == 'archive_date_title':
        current_el = e.text.split(', ')[1].lower().split(' ')[1]
        if len(current_el) == 1:
          current_el = '0' + current_el
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