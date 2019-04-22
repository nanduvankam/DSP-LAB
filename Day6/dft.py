import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
x=[1.0/3.0,1.0/3.0,1.0/3.0,0.0]
N=len(x)
w=(2*np.pi)/N
y=[]
for k in range(0,N):
	sum=0
	for n in range(0,N):
		sum=sum+(x[n]*(np.exp(-j*w*n*k)))
	y=np.append(y,sum)
print(y)
p1=np.abs(y)
plt.subplot(2,1,1)
plt.stem(p1)
p2=np.angle(y)
plt.subplot(2,1,2)
plt.stem(p2)
plt.show()
