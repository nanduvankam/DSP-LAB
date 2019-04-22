import numpy as np
from matplotlib import pyplot as plt
x=np.arange(0,300)
x1=np.sin(2*np.pi*20*x/400)
N=np.random.rand(x1.shape[0])
s=len(x1)
e=N+x1
p=len(e)
p1=np.zeros(s)
for i in range(0,s):
	p1[i]=s[p-i-1]
print p1[i]

d=np.zeros(p)
for i in range(0,p):
	d[i]=(e[b-i-1])
print(d)
h=[1.0/3.0,1.0/3.0,1.0/3.0]
m=np.convolve(s,h)
p2=np.convolve(s,p1)
print(m)
plt.subplot(6,1,1)
plt.plot(x1)
plt.subplot(6,1,2)
plt.plot(N)
plt.subplot(6,1,3)
plt.plot(e)
y1=np.convolve(h,e)
y2=np.convolve(x1,revx)
y3=np.convolve(e,d)
plt.subplot(6,1,4)
plt.plot(y1) #moving average
plt.subplot(6,1,5)
plt.plot(y2)
plt.subplot(6,1,6)
plt.plot(y3)
plt.show()
