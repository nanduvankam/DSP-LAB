import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import numpy as np
fs,data=wav.read('nanvoice.wav')
fs1,data1=wav.read('nanvoice.wav')
fs11,data11=wav.read('nanvoice.wav')
print(fs,fs1)
t=np.arange(0,len(data)/fs,1.0/fs)
t1=np.arange(0,len(data1)/fs1,1.0/fs1)
t11=np.arange(0,len(data11)/fs11,1.0/fs11)
print (t11,len(t11),len(data11))
plt.subplot(311);plt.plot(t1,data1);
plt.subplot(312);plt.plot(t11,data11);
plt.subplot(313);plt.plot(t,data);
plt.show()

