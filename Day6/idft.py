import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
y=[1.0,-j/3.0,1.0/3.0,j/3.0]
N=len(y)
w=(2*np.pi)/N
x=[]
for n in range(0,N):
	sum=0
	for k in range(0,N):
		sum=sum+((y[k]*(np.exp(j*w*n*k)))/N)
	x=np.append(x,sum)
print(x)
p1=np.abs(x)
plt.stem(p1)
plt.show()
