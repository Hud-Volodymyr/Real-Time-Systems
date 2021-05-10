from DFT import w
import numpy as np


def fft(signal):
    N = len(signal)
    length = int(N / 2)
    spectre = np.zeros(N, dtype=complex)
    e_indices = signal[::2]
    o_indices = signal[1::2]
    for p in range(N):
        odds = 0
        evens = 0
        for k in range(length):
            wpk = w(p, k, length)
            odds += o_indices[k] * wpk
            evens += e_indices[k] * wpk
        wpk_odd = w(1, p, N)
        spectre[p] = evens + wpk_odd * odds
    return spectre
