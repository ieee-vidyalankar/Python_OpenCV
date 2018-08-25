# First Link
# download the article
# add that article to list
# load current page
# pause
# check condition

def continue_crawl(previous_url,target_url,max_steps=25):
	if previous_url[-1]==target_url:
		print("Target article Found")
		return False
	elif len(previous_url)>=max_steps:
		print("Too many searches. Abort!")
		return False
	elif previous_url[-1]==previous_url[:-1]:
		print("It's a loop. Abort!")
		return False
	else:
		return True
'''
article_chain =['Hello']
url = "Hello"
print(continue_crawl(article_chain,url))
'''


