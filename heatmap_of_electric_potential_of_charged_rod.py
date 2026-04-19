from numpy import *
from pylab import *

# list
matrix =[]

# function
def f(x,x_prime,y):
    return 1/sqrt((x-x_prime)**2 + y**2)

# integral
def integral(x,y):
    N = 1000
    a = -1
    b = 1
    h = (b-a)/N
    s = f(x,a,y) + f(x,b,y)
    for k in range(1,int(N/2)+1):
        s += 4*f(x,a+(2*k-1)*h,y)
    for k in range(1,int(N/2)):
        s += 2*f(x,a+2*k*h,y)
    return h*s/3

# simulation
for y in arange(5,-5,-0.1):
    line = []
    for x in arange(-5,5,0.1):
        T= integral(x,y)
        line.append(T)
    matrix.append(line)
# graphic
imshow(matrix,extent=[-4,4,-4,4],cmap='inferno')
colorbar(label='Electric Potential(V)')
title('Heatmap of Electric Potential of Charged rod')
xlabel('x(meters)')
ylabel('y(meters)')

show()