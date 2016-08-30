from flask import Flask, render_template, request, redirect
import requests
import json
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.embed import file_html, components
from bokeh.resources import CDN

import random

key = ''



def datetime(x):
    return np.array(x, dtype=np.datetime64)

def saveData(p,**kwargs):
	data = Dict()
	print(p)

def get_random_color(pastel_factor = 0.5):
    return [(x+pastel_factor)/(1.0+pastel_factor) for x in [random.uniform(0,1.0) for i in [1,2,3]]]

"https://www.quandl.com/api/v3/datasets/FRED/GDP/data.json?rows=1"

app = Flask(__name__)
app.data={}
@app.route('/')
def main():
  return redirect('/index')

@app.route('/graph', methods=['POST'])
def getData():
	print('request')
	print(request)
	url = 'https://www.quandl.com/api/v3/datasets/WIKI/'+request.form['st']+'.json?api_key=ozdtgQ9DzyK9ReqsWs-E'
	req = requests.get(url)
	json_data = json.loads(req.text)
	# print(json_data)
	# print(' ')
	stockColumns = ('Date','Open','High','Low','Close','Volume','Ex-Dividend','Split Ratio','Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume')
	df = pd.DataFrame(json_data['dataset']['data'], columns=stockColumns)
	print('test')
	plot = figure(plot_width=400, plot_height=400, x_axis_type="datetime", title="Stock Prices")
	
	for column in request.form.getlist('features'):
		color = "#%06x" % random.randint(0, 0xFFFFFF)
		plot.line(datetime(df['Date']),df[column], color=color, legend=column)
	plot.legend.location = "top_left"

	figJS,figDiv = components(plot,CDN)
	return render_template('/index.html', figJS=figJS, figDiv=figDiv)

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
