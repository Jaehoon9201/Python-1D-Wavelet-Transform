# Reference : https://www.youtube.com/watch?v=Qryd7z9k8i4
# by Dr. Ajay Kumar Verma

from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import pywt

samplerate, data = wavfile.read('DATA.wav')
print(data.shape)
t = np.arange(len(data))/float(samplerate)
data = data/max(data)

cA, cD  = pywt.dwt(data, 'bior6.8', 'per')

y = pywt.idwt(cA, cD, 'bior6.8', 'per')

wavfile.write('DATA_IDWT.wav',samplerate, y)
wavfile.write('DATA_cD.wav', samplerate, cD)

L = len(data);
y=y[0:L];

plt.figure(figsize = (20,35));

plt.subplot(4,1,1)
plt.plot(t, data, color = 'k')
plt.xlabel('Time')
plt.ylabel('S')
plt.title('Original Signal')

plt.subplot(4,1,2)
plt.plot(cA, color = 'r')
plt.xlabel('Samples')
plt.ylabel('cA')
plt.title('Approx Coeff (cA)')


plt.subplot(4,1,3)
plt.plot(cD, color = 'g')
plt.xlabel('Samples')
plt.ylabel('cD')
plt.title('Detailed Coeff (cD)')

plt.subplot(4,1,4)
plt.plot(t, y, color = 'b')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Reconstructed Signal')

plt.savefig('plot.png', dpi = 100)
# plt.show()