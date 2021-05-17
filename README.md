# Python-1D-Wavelet-Transform
[Reference](https://www.youtube.com/watch?v=Qryd7z9k8i4)

In this code, for doing a wavelet transform, Open source library - PyWavelts is used. 

More details about PyWavelets can be found [here](https://pywavelets.readthedocs.io/en/latest/).

## Printing Original Siganl
I loaded the short **DATA.wmv** voice file with this code. 

Below graph shows the voice magnitude in a time domain.
![image](https://user-images.githubusercontent.com/71545160/118479785-6849da00-b74c-11eb-8bfc-7e1b2608167f.png)

## Approxmated Coefficients
The code related to here is like below.

**pywt.dwt** performs a wavelet transform. 
```python
cA, cD  = pywt.dwt(data, 'bior6.8', 'per')
```
![image](https://user-images.githubusercontent.com/71545160/118479810-6ed85180-b74c-11eb-9f01-7b1ec5f4c0e6.png)

## Detailed Coefficients 
The code related to here is like below.
```python
cA, cD  = pywt.dwt(data, 'bior6.8', 'per')
```
![image](https://user-images.githubusercontent.com/71545160/118479827-726bd880-b74c-11eb-8bcd-eb25d942afe3.png)

## Reconstructed Signal
It print the signal after inverse wavelet transform.

The code related to here is like below.
```python
y = pywt.idwt(cA, cD, 'bior6.8', 'per')
```
![image](https://user-images.githubusercontent.com/71545160/118479844-75ff5f80-b74c-11eb-84c0-9cf13dbee265.png)
