from flask import Flask,render_template,request
import math
import re
from collections import Counter
import random
import pygal    

WORD = re.compile(r"\w+")

def open_file(fname):
    f = open(fname)
    lines =f.read()
    return lines

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def form():
	if request.method == 'POST':
		q = request.form['q']
		text1 = open_file('D1.txt')
		text2 = open_file('D2.txt')
		text3 = open_file('D3.txt')
		text4 = open_file('D4.txt')
  
		vectorQ = text_to_vector(q)
		vector1 = text_to_vector(text1)
		vector2 = text_to_vector(text2)
		vector3 = text_to_vector(text3)
		vector4 = text_to_vector(text4)	
 
		cosine1 = get_cosine(vectorQ, vector1)
		cosine2 = get_cosine(vectorQ, vector2)
		cosine3 = get_cosine(vectorQ, vector3)
		cosine4 = get_cosine(vectorQ, vector4)

		pie_chart = pygal.Pie()
		pie_chart.title = 'Graphical Representation'
		pie_chart.add('Cosine for D1', cosine1)
		pie_chart.add('Cosine for D2', cosine2)
		pie_chart.add('Cosine for D3', cosine3)
		pie_chart.add('Cosine for D4', cosine4)

		pie = pie_chart.render_data_uri()
  
		return render_template('info.html',q=q , cosine1=cosine1 ,cosine2=cosine2 ,cosine3=cosine3 , cosine4=cosine4 , pie=pie)
	return render_template('form.html')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)



    
if __name__ == '__main__':
	app.debug = True # el line da byt7at wna b3ml coding 3shan kol ma a3ml save y3ml reload w y update el page
	app.run()