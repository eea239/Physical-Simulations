from numpy import *
from pylab import *

# constants
lambda0 = 500.0
N = 50
k = 2*pi/lambda0


# screen
physical_extent = 1000.0
resolution = 500
x_scale =linspace(-physical_extent,physical_extent,resolution)
intensity = zeros([500,500])

# screen
x_axis = linspace(-100,100,500)
y_axis = linspace(-100,100,500)


# bessel function
def Jm(x,theta):
    return cos(theta-x*sin(theta))/pi

# integral
def integral(x):
    a = 0.0
    b = pi
    x_standard,w_standard = polynomial.legendre.leggauss(N)

    # mapping
    xp = 0.5*(b-a) * x_standard + 0.5 * (b+a)
    wp = 0.5*(b-a) * w_standard

    integral_result = sum(wp*Jm(x,xp))
    return integral_result

# rotate pixel
for i in range(500): # Y-axis (Rows)
    for j in range(500): # X-axis (column)
        x = x_axis[j]
        y = y_axis[i]
        # calculate r
        r = sqrt(x**2 + y**2)
        # If r=0, we use if/else to avoid errors
        if r < 1e-5:
            intensity[i,j] = 1.0
        else:
            optical_scale = 20.0  # We pull it back to fit the screen
            bessel_arg = optical_scale * k * r
            value = integral(bessel_arg)
            intensity[i,j] = (2*value/ bessel_arg)**2

# graphic1
figure(figsize=(14,6))
subplot(1,2,1) # Airy Diffraction pattern (heatmap)
pattern=imshow(intensity,extent=[-physical_extent,physical_extent,-physical_extent,physical_extent],cmap='inferno',vmin=1e-3,vmax=0.05)
title('Airy Disc Diffraction Pattern')
xlabel('X(nm)')
ylabel('Y(nm)')
colorbar(pattern,label='Normalized Intensity')

#graphic2
subplot(1,2,2)
center_line = intensity[int(resolution/2),:]
plot(x_scale,center_line,color='red',linewidth=2)
title('Intensity Profile')
xlabel('X distance(nm)')
ylabel('Normalized Intensity')
grid(True)
ylim(0,1.1)

tight_layout() # Adjusts spacing so graphics don't interfere with each other
show()

