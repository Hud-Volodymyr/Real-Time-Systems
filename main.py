from random_signals import signal_generator
from DFT import discrete_fourier_transform
import matplotlib.pyplot as plotter

n = 14
w = 2000
N = 264

signal = signal_generator(n, w, N)
spectre = discrete_fourier_transform(signal)

figure, axis = plotter.subplots(2, 1)

plotter.subplots_adjust(left=0.1, top=0.9, bottom=0.1, right=0.99, hspace=0.5)

axis[0].plot(range(N), signal)
axis[0].set_title("Сигнал")
axis[0].set(xlabel='Час', ylabel='Згенерований сигнал')

axis[1].plot(range(N), spectre)
axis[1].set_title("Дискретне перетворення Фур'є")
axis[1].set(xlabel='p', ylabel='F(p)')
plotter.show()
