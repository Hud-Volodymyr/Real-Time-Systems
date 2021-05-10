from random_signals import signal_generator
from FFT import fft
import matplotlib.pyplot as plotter
import numpy as np

n = 14
w = 2000
N = 256


signal = signal_generator(n, w, N)

spectre = abs(fft(signal))


figure, axis = plotter.subplots(2, 1)

plotter.subplots_adjust(left=0.1, top=0.9, bottom=0.1, right=0.99, hspace=0.5)

axis[0].plot(range(N), signal)
axis[0].set_title("Сигнал")
axis[0].set(xlabel='Час', ylabel='Згенерований сигнал')

axis[1].plot(range(N), spectre)
axis[1].set_title("Швидке перетворення Фур'є")
axis[1].set(xlabel='p', ylabel='F(p)')
plotter.show()



