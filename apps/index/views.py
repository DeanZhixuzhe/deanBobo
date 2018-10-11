from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from datetime import datetime
import time
import math
from django.db import connection
from django import forms
import requests
import urllib3
from bs4 import BeautifulSoup
# from spider import server
from spider.server import *
import threading
# Create your views here.

# class Person(object):
# 	"""docstring for Person"""
# 	def __init__(self, username):
# 		super(Person, self).__init__()
# 		self.username = username
		
def index(request):
	# cursor = connection.cursor()
	# cursor.execute("select * from lottery")
	# l = cursor.fetchall()
	# print(l)
	# username = request.GET.get('username')
	context = {
		# 'username' : 'sjdlf',
		'lottery' : [
			{
				'name' : '腾讯分分彩',
				'code' : 'txffc',
				'saletime' : '0000-2359',
				'open_frequency' : '60',
			},
			{
				'name' : '重庆时时彩',
				'code' : 'cqssc',
				'saletime' : '0900-0200',
				'open_frequency' : '600',
			}
		],
		# 'greet' : greet,
		'today' : datetime.now(),
		# 'lotterys' : l,
	}
	# if username:
	# 	return render(request,'default\pc\index.html',context=context)
	# else:
	# login_url = reverse('index:login')
	return render(request,'default/pc/index.html',context=context)
def greet(word):
	return "Hello Word{}".format(word)

def login(request):
	return HttpResponse("这是一个登陆会员的页面")

def txffc(request):
	return HttpResponse("腾讯分分彩") 

def cqssc(request):
	return HttpResponse("重庆时时彩")

def lottery(request):
	return render(request,'default/pc/lottery.html')

class Fankui(forms.Form):
	"""docstring for Fankui"""
	yourname = forms.CharField(label='Your name',max_length=100)

def fankui(request):
	form = Fankui()
	return render(request,'default/pc/kui.html',{'form':form})

def caiji(request):
	url = "http://www.off0.com/index.php"
	result = requests.get(url)
	
	# result.content.decode('gb2312')
	# print(result)
	# result = unicode(result,'utf-8')
	result.encoding = 'utf-8'
	soup = BeautifulSoup(result.content).select('table tr')
	table = soup
	# print(table)
	
	# arr2 = []
	# for tr in table:
	# 	arr = []
	# 	for td in tr:
	# 		# arr += td.string
	# 		arr.append(td.string)
	# 		print(td.string)
	# 		# print(arr)
	# 	arr2.append(arr)
	# 	print(arr2)
	# title = soup.select('h1')
	# con = soup.select('div.art-text')
	# hotnews = soup.select('.hotnews-list a')
	# print(type(hotnews[1]['href']))
	l = []
	# for link in hotnews:
		# l += link['href']
	# print(hotnews[1])
	# res = server.Serveri.get_table(url)
	res = Serveri.get_table(url)
	# print(res)
	# t = threading.Timer(10,caiji)
	# t.start
	return HttpResponse(res)
if __name__ == "__main__":
	caiji()