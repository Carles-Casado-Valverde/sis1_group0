import numpy as np

def envelope(x, N):
    w = np.abs(x)
    b = [1.0/N]*N
    y = np.convolve(w, b, mode='same')
    return y

def synthetize(f0, phi, Ak, t):
  y = 0
  for k in range(1, len(Ak) + 1):
    y += Ak[k-1] * np.cos(2*np.pi*k*f0*t + k*phi - (k-1)*np.pi/2)
  return y
