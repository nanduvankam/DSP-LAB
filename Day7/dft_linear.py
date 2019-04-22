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
def sum(x,y):
	z=[]
	for i in range(len(x)):
		s=x[i]+y[i]
		z.append(s)
	return z
	
x1=input("enter seq1:")
f1=dft(x1)
x2=input("enter seq2:")
f2=dft(x2)
s1=sum(f1,f2)
s2=sum(x1,x2)
f3=dft(s2)
print f1
print f2
print s1
print f3


