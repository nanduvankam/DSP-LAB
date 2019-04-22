import matplotlib.pyplot as plt
import numpy as np
f1=100
f2=100
Fs=2000
n=100
y=np.arange(n)
x1=np.cos(2*np.pi*y*f1/Fs)
x2=np.cos(2*np.pi*y*f2/Fs)
x=x1+x2
plt.plot(x)
plt.show()
