from random_signals import signal_generator
from correlations import correlation_list, correlation
from time import time


n = 14
w = 2000
N = 264

x_signal = signal_generator(n, w, N)
y_signal = signal_generator(n, w, N)
start = time()
correlated_array = correlation(x_signal, y_signal, N)
end = time()
print('Час виконання кореляції з масивом: ', end - start)

start = time()
correlated_list = correlation(x_signal, y_signal, N)
end = time()
print('Час виконання кореляції з структурою list(): ', end - start)

