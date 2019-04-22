import numpy as np
import matplotlib.pyplot as plt
n1=input("enter no of elements")
n2=input("enter no of elements")
m=np.linspace(0,100,50)
p=n1+n2-1
x=np.zeros(p)
h=np.zeros(p)
y=np.zeros(p)
for i in range (0,n1,1):
	x[i]=input('enter a element')
for j in range (0,n2,1):
	h[i]=input('enter a element')
for m in range(0,p,1):
	for o in range(0,p,1):
		y[m]=h[0]*x[m-0]
print y
plt.stem(x,h)
plt.show()


