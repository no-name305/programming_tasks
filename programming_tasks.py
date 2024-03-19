#import libs
import requests
from bs4 import BeautifulSoup
import random
#function task parsing
def task_parsing (pages=59):
	#list tasks
	tasks = []
	
	#page parsing loop
	for n in range(pages):
		n += 1
		
		#get page
		url = f'https://proglang.su/tasks/page-{n}'
		session=requests.session()
		headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
		page=session.get(url,headers=headers)
		soup = BeautifulSoup (page.text, 'html.parser')
		
		#get task
		result = BeautifulSoup (str(soup.findAll('div',class_='col-lg-6')), 'html.parser').find_all('p')
		
		#add task in list tasks
		for task in result:
			tasks.append(task.text)
	return tasks
