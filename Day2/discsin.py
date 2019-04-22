import matplotlib.pyplot as plt
import numpy as np
Fs=300
f=5
sample=200
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.stem(x,y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()