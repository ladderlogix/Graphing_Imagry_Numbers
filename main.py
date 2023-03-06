# import libraries
import matplotlib.pyplot as plt
import numpy as np

# create data of complex numbers
data = np.array([-1.43449-1.0204j, -1.13036-0j, -1.4349+1.0204j, 0.16664-0.95193j, 0.16664+0.95193j, 1.33344-0.23921j])

# extract real part using numpy array
x = data.real
# extract imaginary part using numpy array
y = data.imag

# plot the complex numbers
plt.grid(True)
plt.axhline(0,color='black') # x = 0
plt.axvline(0,color='black') # y = 0
plt.plot(x, y, 'g*')
for i in range(0, len(x)):
    plt.plot((x[i],0), (y[i],0), 'ro-')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()