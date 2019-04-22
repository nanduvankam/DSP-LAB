import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
w=np.linspace(0,2*np.pi,1000)
x=[1.0/3.0,1.0/3.0,1.0/3.0,0.0]
y=[]
y=np.zeros(1000)
l=len(x)
for i in range(0,1000):
	sum=0
	for n in range(0,l-1):
		sum=sum+(x[n]*(np.exp(-j*w[i]*n)))
		y[i]=sum
	y=np.append(y,sum)
print(y)
p=np.abs(y)
plt.subplot(2,1,1)
plt.plot(p)
q=np.angle(y)
plt.subplot(2,1,2)
plt.plot(q)
plt.show()
