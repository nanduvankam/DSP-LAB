import numpy as np
import matplotlib.pyplot as plt
M=input("enter M:")
n=np.arange(0,M)
p=(M-1)/2.0
k=np.abs(n-p)
a=k/(M-1)
b=2*a
y=1-b
plt.stem(y)
plt.show()
