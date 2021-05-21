from random_signals import signal_generator
from correlations import autocorrelation, correlation
import matplotlib.pyplot as plotter

n = 14
w = 2000
N = 264

x_signal = signal_generator(n, w, N)
xx_correlated = autocorrelation(x_signal, 264)
y_signal = signal_generator(n, w, N)
xy_correlated = correlation(x_signal, y_signal, 264)

plotter.plot(range(264), xx_correlated)
plotter.title("Автокорляція сигналу")
plotter.xlabel("τ")
plotter.ylabel("Автокореляційна функція")
plotter.show()

plotter.plot(range(264), xy_correlated)
plotter.title("Кореляція двох сигналів")
plotter.xlabel("τ")
plotter.ylabel("Кореляційна функція")
plotter.show()
