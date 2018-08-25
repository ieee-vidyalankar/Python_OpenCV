###################### Without sets #######
def remove_duplicates(list_name):
	new_city = []
	for item in list_name:

		if item not in new_city:
			new_city.append(item)
		
		
	return new_city



def main():
	old_city =['Mumbai','Mumbai','Thane','Mumbai','Wadala','Mumbai','Thane']
	
	x =remove_duplicates(old_city)
	print(x)
	#print(len(x))



main()

######################## using sets ############ 
   # sets are used to store unique elements (by default)
   
city_name = ['Pune','Nashik','Mumbai','Mumbai']

city_set = set(city_name)

print(city_set)

city_set.add('Wadala')  #set_function

print(city_set)




		
		







