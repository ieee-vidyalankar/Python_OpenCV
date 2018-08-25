#################DICTIONARIES########

##ORDER NOT DEFINED##

#use to store pair of elements: Keys and Values
city_name ={24:8,'Pune':34,'Thane':2}
x = city_name[24]
print(x)
y= city_name['Pune']
print(y)
city_name['Paune']=444
print(city_name['Paune'])
print(city_name)

city_namez ={24:8,'Pune':34,'Thane':2}
x =city_namez.get('Punes','It\'s an invalid element') # get is dict_function
print(city_name.get('hi')) #return None
print(x)
print(city_namez)

#############################



