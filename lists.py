''' LISTS ARE MUTABLE '''
############################

lists =[2,3,4,5,6] 	#declare list
lists[2:]=10,11,12 		#update list
print(lists[0:])  #list slice
#print(len(lists))
string_name = "Hello World"
print("str o/p is"+string_name[5:])  #string slice # Note: string cannot be updated!
print('Hello' in string_name) # return boolean value

##############################

def top_three(input_list):
	new_list = sorted(input_list,reverse=True)
	print(new_list)
	print(new_list[:2])
	print(sorted(input_list))
	print(input_list[:])  # to verify that the original list order is unchanged
top_three(input_list=[2,3,5,6,8,4,2,1])

###################################


jack =[1,2,34,0]
jack.append(3)
print(len(jack))
print(jack)
if 34 in jack:
	print("hi")

#######################################


