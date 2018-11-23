import numpy as np 
import matplotlib.pyplot as plt 

x = np.loadtxt('x_x.dat')
y_0 = np.loadtxt('y_0x.dat')
y_0OPEN = y_0

plt.figure()
plt.subplot(211)
plt.plot(x, y_0, label='Serial')
plt.legend()

plt.subplot(212)
plt.plot(x, y_0OPEN, label='Paralelizado')
plt.legend()

plt.savefig('Advection.pdf')

walk = np.loadtxt('walk.dat')
walkOPEN = np.loadtxt('walkOPEN.dat')

plt.figure()

plt.subplot(211)
plt.hist(walk, bins=100, label='Serial')
plt.legend()

plt.subplot(212)
plt.hist(walkOPEN, bins=100, label='Serial')
plt.legend()

plt.savefig('walk.pdf')

