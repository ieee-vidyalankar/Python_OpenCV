###########################

from bs4 import BeautifulSoup
import requests
response = requests.get("https://en.wikipedia.org/wiki/Philosophy") #request the web server for access
#print(response)
html =response.text                 #convert the object into text format
#print(html)

soup = BeautifulSoup(html,'html.parser') #soup object created
#print(soup.title)
#print(soup.script)
for link in soup.find_all('a'):  #find all tags <a></a>
	#print("link is " + str(link)) 
	#print(link.get('href'))         #find the keyword in links(here: eg <a> tag)
	print(soup.find_all('a'))
print(soup.head.title)

##############################

from bs4 import BeautifulSoup
file_name = "F:/Udacity/HTML and CSS/mypage.html"
with open(file_name) as f:
	soup = BeautifulSoup(f,'html.parser')
print(soup.ul.li)
print("Soup starts here \n" +str(soup))

##############################
