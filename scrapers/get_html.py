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