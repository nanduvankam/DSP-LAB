import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x):
	j=cm.sqrt(-1)
	N=len(x)
	w=(2*np.pi)/N
	y=[]
	for k in range(0,N):
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*n*k))
		y=np.append(y,sum)
	print(y)
	return y
x=[1.0/3.0,1.0/3.0,1.0/3.0,0]
y1=dft(x)
print "output1",y1
j=cm.sqrt(-1)
N=len(x)
h=[]
w=(2*np.pi)/4
for n in range(0,N):
	s=np.exp(j*w*n)*x[n]
	h=np.append(h,s)
f=dft(h)
print "shifted",f

