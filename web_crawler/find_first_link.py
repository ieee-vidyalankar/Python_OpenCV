# download html of last_article in article_chain
# find first link in that html
# add first link to article_chain
# delay for about 2 seconds

import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Spanish_language')        #download the page
#print(response)  
html_file = response.text                                               # change to text
soup = BeautifulSoup(html_file,'html.parser')							# create soup object of the html file
#print(data)

 ########## ITERATION 1 ############## 

#first_id =soup.find(id='mw-content-text').find(class_='mw-parser-output').p.a.get('href')  ######first anchor tag in first para of div with id=" "  !! DOES NOT WORK FOR ALL !!#####
#print(first_id)
#for link in soup.find_all('a'):
	#print(link.get('href'))


########### ITERATION 2 ###############  #ISSUE SOLVED : skip to direct descendants paragraph
'''
div = soup.find(id='mw-content-text').find(class_='mw-parser-output')
for element in div.find_all('p',recursive=False):            # If direct paragraph is present then return run for loop (TRUE)
	#print(element)
	#print(element.a)
	if element.a:											# if first anchor tag is present (TRUE) : then go ahead to load its reference and then BREAK
		first_link = element.a.get('href')						
		break												
print(first_link)
'''
######### ITERATION 3 ###############     #ISSUE SOLVED : footnotes are not direct anchor tag descendants

wanted_div =soup.find(id='mw-content-text').find(class_='mw-parser-output')
for element in wanted_div.find_all('p',recursive=False):         
	#print(str(element) +" \n this is element \n")
	if element.find('a',recursive=False):					#run only if direct anchor tag is present (note: recursice:fals = direct)
		#print(element.find('a',recursive=False))
		first_link = element.find('a',recursive=False).get('href')   #get the reference of the first tag and quit
		break
		
print(first_link)

'''
import requests
from bs4 import BeautifulSoup

 ############################# FUNCTION #############

def find_first_link(url):
	response = requests.get(url)        #download the page
	#print(response)  
	html_file = response.text                                               # change to text
	soup = BeautifulSoup(html_file,'html.parser')							# create soup object of the html file
	#print(data)

	wanted_div =soup.find(id='mw-content-text').find(class_='mw-parser-output')
	for element in wanted_div.find_all('p',recursive=False):         
		#print(str(element) +" \n this is element \n")
		if element.find('a',recursive=False):					#run only if direct anchor tag is present (note: recursice:fals = direct)
			#print(element.find('a',recursive=False))
			first_link = element.find('a',recursive=False).get('href')   #get the reference of the first tag and quit
			break
	return(first_link)
#print(first_link)

'''

