import numpy as np
import matplotlib.pyplot as plt
M=32
n=np.arange(0,M-1)
x1=np.cos(2*np.pi*n/(M-1))
w=0.54-0.4*x1
plt.stem(n,w)
plt.show()