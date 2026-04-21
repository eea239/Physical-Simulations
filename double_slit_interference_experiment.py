from numpy import *
from pylab import *

# list
matrix =[]

# constants
lambda0 = 5.0
k = 2*pi/lambda0
# first wave source
x1 = 1.0
y1 = 0.0
# second wave source
x2 = -1.0
y2 = 0.0

# function
def f(x,y):
    A = 1
    r1 = sqrt((x-x1)**2+(y-y1)**2)
    r2 = sqrt((x-x2)**2+(y-y2)**2)
    return A*(sin(k*r1)+sin(k*r2))

# simulation
for y in arange(20,-20,-0.1):
    line = []
    for x in arange(-20,20,0.1):
        wave = f(x,y)
        line.append(wave)
    matrix.append(line)

# graphic
imshow(matrix,extent=[-20,20,-20,20],cmap='gray')
title('Double-Slit Interference Experiment')
xlabel('x(meters)')
ylabel('y(meters)')

show()

