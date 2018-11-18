import requests
from bs4 import BeautifulSoup
import urllib
import time

target_url ='https://en.wikipedia.org/wiki/Science'
start_url ="https://en.wikipedia.org/wiki/Sachin_Tendulkar"

 #############################
def find_first_link(url):
	response = requests.get(url)        #download the page
	#print(response)  
	html_file = response.text                                               # change to text
	soup = BeautifulSoup(html_file,'html.parser')							# create soup object of the html file
	#print(data)

	wanted_div =soup.find(id='mw-content-text').find(class_='mw-parser-output')
	article_link =None
	for element in wanted_div.find_all('p',recursive=False):         
		#print(str(element) +" \n this is element \n")
		if element.find('a',recursive=False):					#run only if direct anchor tag is present (note: recursice:false = direct)
			#print(element.find('a',recursive=False))
			article_link = element.find('a',recursive=False).get('href')   #get the reference of the first tag and quit
			break
	if not article_link:
		return None

	first_link = urllib.parse.urljoin('https://en.wikipedia.org/',article_link)
	return first_link	

#######################

def continue_crawl(previous_url,target_url,max_steps=25):
	if previous_url[-1]==target_url:
		print("Target article Found")
		return False
	elif len(previous_url)>max_steps:
		print("Too many searches. Abort!")
		return False
	elif previous_url[-1]==previous_url[:-1]:
		print("It's a loop. Abort!")
		return False
	else:
		return True

##################################################


article_chain = [start_url]

while continue_crawl(article_chain,target_url):
	print(article_chain[-1])

	first_link =find_first_link(article_chain[-1])
	if not first_link:
		print("No further links found!")
	article_chain.append(first_link)
	time.sleep(0.2)
print(article_chain[-1])