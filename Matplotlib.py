#Install Matplotlib = pip3 install matplotlib
import matplotlib
import matplotlib.pyplot as plot #matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. 
import numpy as np
from pylab import *
#1.
x = np.linspace(0,5,10) #10 samples point from 0 to 5
print(x)                #will print the array
print(type(x))          #numpy array
y = x**2                #the equation y is x raised to 2

figure()

plot(x,y,'r')           #(x-axis,y-axis,color)
xlabel('timesample')
ylabel('temperature values')
title('my first graph')
show()

#subplot
subplot(1,2,1)          #1 row 2 column 1st(nrows, ncloumns, index)
plot(x,y,'r--')
subplot(1,2,2)
plot(y,x,'g*-')
show()

#2.
x = np.linspace(0,5,10) 
print(x)
print(type(x))
y = x**2

fig = plt.figure()                     #<plt.class>
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #<add_axes is a object> & [x-axis,y-axis,length,breadth]
axes.plot(x,y,'r')                     #object.function
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
axes.set_title('xyz')
plt.show()