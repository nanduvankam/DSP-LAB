import numpy as np
import matplotlib.pyplot as plt
M=32
n=np.arange(0,M-1)
x1=np.cos(2*np.pi*n/(M-1))
x2=np.cos(4*np.pi*n/(M-1))
w=0.42-0.5*x1+0.08*x2
plt.stem(n,w)
plt.show()