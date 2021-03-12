import numpy as np


def w(p, k, N):
    internal = 2 * np.pi * p * k / N
    return complex(np.cos(internal), np.sin(internal))


def discrete_fourier_transform(signal):
    N = len(signal)
    spectre = np.zeros(N)
    for p in range(N):
        sum = 0
        for k in range(N):
            xk = signal[k]
            wpkN = w(p, k, N)
            sum += xk * wpkN
        spectre[p] = abs(sum)
    return spectre
