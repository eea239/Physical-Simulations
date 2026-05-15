from numpy import *
from pylab import *

# constants

planck_constant = 6.62607004e-34
c = 3e8
boltzmann_constant = 1.38064852e-23

# list
energy_levels = []


# function
def I(lambda0,T):
    return (2 * planck_constant * c**2) / (lambda0**5) * (1 / (exp((planck_constant * c) / (lambda0 * boltzmann_constant * T)) - 1))

# integral
def integral(T):
    N = 50
    b = 1e-5
    a = 1e-9
    x_standard,w_standard = polynomial.legendre.leggauss(N)

    # mapping
    xp = 0.5 * (b - a) * x_standard + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w_standard

    integral_result = sum(wp*I(xp,T))
    return integral_result

# loop
T_value = linspace(3000,10000,100)
for T in T_value:
    total_energy = integral(T)
    energy_levels.append(total_energy)

# graphic
plot(T_value**4,energy_levels,color='red',linewidth=2)
title('Planck Radiation and Stefan-Boltzmann law')
xlabel('Temperature (K)')
ylabel('Energy')
grid(True)
show()
