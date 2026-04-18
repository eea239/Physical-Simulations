from numpy import *
from pylab import *

# lists
tested_angles =[]
real_periods =[]
approximate_periods=[]

# constant
L = 10
g = 9.8

# function
def f(x,theta0):
    return 1/sqrt(1-(sin(theta0/2))**2 * (sin(x)**2))

# integral
def integral(theta0):
    N = 1000
    a = 0
    b = pi/2
    h = (b-a)/N
    s = f(a,theta0)+f(b,theta0)
    for k in range(1,int(N/2)+1):
        s += 4*f(a+(2*k-1)*h,theta0)
    for k in range(1,int(N/2)):
        s += 2*f(a+2*k*h,theta0)

    return h*s/3


# simulation
for theta0 in range(1,171):
    tested_angles.append(theta0)
    theta0_radians = radians(theta0)
    T = 2*pi*sqrt(L/g)
    approximate_periods.append(T)
    result_of_integral = integral(theta0_radians)
    conclusion = result_of_integral * 4*sqrt(L/g)
    real_periods.append(conclusion)

# Graphics
plot(tested_angles,real_periods,label='Real Period',color='red',linewidth=2)
plot(tested_angles,approximate_periods,label='Approximate Period',color='blue',linestyle='--')
title('Pendulum period vs. Initial angle')
xlabel('Tested Angles')
ylabel('Period')
legend()
grid(True)

show()