import numpy as np
x=np.array(input("enter 1st seq:"))
h=np.array(input("enter 2nd seq:"))
n1=len(x)
n2=len(h)
l=n1+n2-1
z=np.zeros(l)
for n in range(0,l):
	y=0
	for k in range(0,n1):
		if (n-k)<n2 and (n-k)>=0:
		        y=y+x[k]*h[n-k]
		z[n]=y
print z	