import numpy as np
x=np.array(input("enter 1st seq:"))
h=np.array(input("enter 2nd seq:"))
n1=len(x)
n2=len(h)
l=n1+n2-1
l1=max(n1,n2)
z=np.zeros(l+1)
for n in range(0,l):
	y=0
	for k in range(0,n1):
		if (n-k)<n2 and (n-k)>=0:
		        y=y+x[k]*h[n-k]
		z[n]=y
print z	
s=[]
for i in range(l1,l):
	p=z[i]+z[i-4]
	s=np.append(s,p)
h1=z[3]
s=np.append(s,h1)
print s
