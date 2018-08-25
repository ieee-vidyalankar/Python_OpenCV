########### Using Modules ----01----- ##################
'''Topics covered : 1)Functions
			 	    2)Classes and objects
				    3)Loops - For loop 
'''
import turtle
import time

def draw_square(obj):
	for x in range(0,4):
		obj.forward(100)
		obj.right(90)
		time.sleep(0.5)




def main():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.color("yellow")
	brad.shape("turtle")
	for x in range(0,1):
		brad.speed(30)
	draw_square(brad)
	window.exitonclick()
main()
