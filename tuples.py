########### Tuples are immutable, Cant add or remove items ##################

related_info = (12,13,14)  # with or without parenthesis
print(related_info[2])
l,b,h = related_info	# tuple unpacking
print( "dimensions are {}x{}x{}".format(l,b,h))


#######################

world_locations = { (222, 111) : "Taj" , (12.1,213) : "hsa" } #tuples as dict 'keys' (since immutable)
print(world_locations[12.1,213])

def color(tuple_name):  # tuple used to return multiple values
	return tuple_name[0], tuple_name[2]
color_names = "blue","red","black"  #tuple declared
a = color(color_names)
print(a)
 
####################

def hours2days(input_hours):
	days = input_hours//24
	hours = input_hours -days*24
	return days,hours

a = hours2days(33)
print(a)
