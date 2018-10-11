import requests
from bs4 import BeautifulSoup

class Serveri():
	"""docstring for ClassName"""
	
		
	def get_table(url,code='utf-8'):
		gather = requests.get(url)
		gather.encoding = code
		table = BeautifulSoup(gather.content).select('table tr')
		result = []
		for tr in table:
			tds = []
			for td in tr:
				tds.append(td.string)
			result.append(tds)
		return result