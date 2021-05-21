import numpy as np


def expectation(signal):
    sig_sum = 0
    for i in range(len(signal)):
        sig_sum += signal[i]
    expect = sig_sum / len(signal)
    return expect


def correlate(x, y, t):
    x_expectation = expectation(x)
    y_expectation = expectation(y)
    x_length = len(x)
    sig_sum = 0
    for time in range(x_length - t):
        sig_sum += (x[time] - x_expectation) * (y[time + t] - y_expectation)
    corr = sig_sum / (x_length - 1)
    return corr


def correlation(x, y, step):
    correlations = np.zeros(step)
    for t in range(step):
        correlations[t] = correlate(x, y, t)
    return correlations


def correlation_list(x, y, step):
    correlations = list()
    for t in range(step):
        correlations.append(correlate(x, y, t))
    return correlations


def autocorrelation(x, step):
    return correlation(x, x, step)
