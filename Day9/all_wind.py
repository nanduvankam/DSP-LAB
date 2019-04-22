import numpy as np
import matplotlib.pyplot as plt
M=input("enter M:")
n=np.arange(0,M-1)
#rect_wind
w=np.ones(M-1)
plt.stem(n,w)
#tri_wind
p=(M-1)/2.0
k=np.abs(n-p)
a=k/(M-1)
b=2*a
y=1-b
plt.stem(y)
#ham_wind
x1=np.cos(2*np.pi*n/(M-1))
w1=0.54-0.4*x1
plt.stem(n,w1)
#han_wind
x2=np.cos(2*np.pi*n/(M-1))
w2=0.5-0.5*x2
plt.stem(n,w2)
#black_wind
x3=np.cos(2*np.pi*n/(M-1))
x4=np.cos(4*np.pi*n/(M-1))
w3=0.42-0.5*x3+0.08*x4
plt.stem(n,w3)
plt.show()
