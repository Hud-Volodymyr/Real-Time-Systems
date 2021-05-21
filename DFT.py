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


def discrete_fourier_transform_table(signal):
    N = len(signal)
    spectre = np.zeros(N)
    wpk_table = np.zeros((N, N), dtype=complex)
    for p in range(N):
        sum = 0
        for k in range(N):
            xk = signal[k]
            wpk_table[p][k] = w(p, k, N)
            sum += xk * wpk_table[p][k]
        spectre[p] = abs(sum)
    #for p in range(N):
    #    print(p, wpk_table[p])
    return spectre
