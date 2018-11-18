from urllib import request,parse
import urllib.parse
import os

def read():
	notepad = open(r"profanity.txt")
	content_file = notepad.read()
	#print(content_file)
	notepad.close()
	profanity_check(content_file)
	
def profanity_check(text_to_check):
	bridge = request.urlopen(r"http://www.wdylike.appspot.com/?q="+parse.quote(text_to_check))
	result= bridge.read()
	#print(result)
	bridge.close()
	if b"true" in result:
		print("Profanity Alert!")
	elif b"false" in result:
		print("No cuss words found")
	else:
		print("Cannot scan the text") 
   



read() 