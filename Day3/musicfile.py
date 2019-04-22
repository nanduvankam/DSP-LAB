import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
fs,data=wav.read('music.wav')
wav.write('low_music.wav',2*fs,data)
print (fs,data,len(data))
plt.plot(data)
plt.show()
