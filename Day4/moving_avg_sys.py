import matplotlib.pyplot as plt
import numpy as np
f1=4
t=np.arange(0,5,0.01)
y1=np.sin(2*np.pi*f1*t)
plt.subplot(4,1,1)
plt.plot(t,y1)

y2=np.random.rand(y1.shape[0])
plt.subplot(4,1,2)
plt.plot(y2)
y=y1+y2
plt.subplot(4,1,3)
plt.plot(y)
p=input("Order of moving avg system:")
s=0
for i in range(int(p-1)):
	s=np.sum(
plt.subplot(4,1,4)
plt.plot(s)
plt.show()

