import matplotlib.pyplot as plt
import numpy as np
Fs=500
f=6
sample=200
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.subplot(3,1,1)
plt.stem(x,y)
Fs1=150
f1=5
sample=200
m=np.arange(sample)
n=np.sin(2*np.pi*f*m/Fs1)
plt.subplot(3,1,2)
plt.stem(m,n)

z=y+n
plt.subplot(3,1,3)
plt.stem(m,z)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()