#Python If ... Else
#Python Conditions and If statements
#1. If
a = 4
b = 5
if a < b:
	print("a is less than b")

#2. Elif
a = 200
b = 100
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")

#3. Nested loop
a = 200
b = 100
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
elif a != b:
	print("a and b are not equal")
else:
	print("a is greater than b")
################################################################

#The  While loop
#1. To print i as long as i is less than 10
i = 1
while i < 10:
	print(i)
	i += 1

#2. With a break statement we can stop the loop even if the condition is true
i = 1
while i < 10:
	print(i)
	if i == 5:
		break
	i += 1

#################################################################

#The For Loop
#1. 
for i in range(5):
	print(i)
#2.
for i in range(3,6):
	print(i)
#3.
for i in range(2,8,2):
	print(i)
#4.
for i in range(0,-10,-2):
	print(i)
#5. Print each element from the list
fruits = ["Apple","Mango","Grapes"]
for i in fruits:
	print(i)
#6. Else in for loop
for i in range(5):
	print(i)
else:
	print("Finished!!!")
#7. Nested for loop
color = ["red","green","black"]
fruits = ["Apple","Pear","Cheery"]
for x in color:
	for y in fruits:
		print(x,y)
#8. Append even numbers in empty list using 'for' and 'if' 
list=[]
for everyVal in range(0,10):
	if everyVal%2==0:
		list.append(everyVal)
print(list)
print(len(list))
