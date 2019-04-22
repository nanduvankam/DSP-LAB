import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dtft(x):
	j=cm.sqrt(-1)
	w=np.linspace(-np.pi,np.pi,10000)
	y=[]
	y=np.zeros(10000)
	l=len(x)
	for i in range(0,10000):
		sum=0
		for n in range(0,l):
			sum=sum+(x[n]*(np.exp(-j*w[i]*n)))
		y1=np.abs(sum)
		y=np.append(y,y1)
	return y
M=32
n=np.arange(0,M-1)
w=np.ones(M-1)
n=np.arange(-17,17)
f=0.25*(np.sinc(0.25*n))
#f[100]=1.0/4.0
f1=dtft(f)
g=[]
for i in range(0,31):
	g1=(f[i]*w[i])
	g=np.append(g,g1)
print g
g3=dtft(g)
a=20*np.log(g3)
print a
plt.subplot(5,1,1)
plt.stem(w)
plt.subplot(5,1,2)
plt.plot(f)
plt.subplot(5,1,3)
plt.plot(f1)
plt.subplot(5,1,4)
plt.plot(g3)
plt.subplot(5,1,5)
plt.plot(a)
plt.show()
