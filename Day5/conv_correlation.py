import numpy as np
from matplotlib import pyplot as plt
x=np.arange(0,300)
x1=np.sin(2*np.pi*20*x/400)
N=np.random.rand(x1.shape[0])
s=N+x1
h=[1.0/3.0,1.0/3.0,1.0/3.0]
m=np.convolve(s,h)
l=len(h)
h1=np.zeros(l)
for i in range(0,l):
	h1[i]=h[l-i-1]
print h1
y=np.convolve(x1,h1)
plt.subplot(5,1,1)
plt.plot(x1)
plt.subplot(5,1,2)
plt.plot(N)
plt.subplot(5,1,3)
plt.plot(s)
plt.subplot(5,1,4)
plt.plot(m)
plt.subplot(5,1,5)
plt.plot(y)
plt.show()