from random_signals import signal_generator
import matplotlib.pyplot as plt


def expectation(signal):
    sig_sum = 0
    for i in range(len(signal)):
        sig_sum += signal[i]
    expect = sig_sum / len(signal)
    return expect


n = 14
w = 2000
N = 264
Mx = [0] * N
Ns = [0] * N
for i in range(1, N):
    N_current = i
    Ns[i] = N_current
    sig_cur = signal_generator(n, w, N_current)
    Mx[i] = expectation(sig_cur)

plt.plot(Ns, Mx)
plt.title("Графік залежності N від Mx")
plt.xlabel("N")
plt.ylabel("Mx")
plt.show()
