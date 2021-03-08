import numpy as np


def generate_signal(amplitude, phase, frequency, time):
    return amplitude * np.sin(frequency * time + phase)  # Press Ctrl+F8 to toggle the breakpoint.


def signal_generator(harmonics, frequency_max, samples_amount):
    signal_collection = np.zeros(samples_amount)
    for f in range(1, harmonics + 1):
        phase = np.random.uniform((-np.pi / 2), (np.pi / 2))
        amplitude = np.random.uniform(0, 1)
        frequency = f * frequency_max / harmonics
        for time in range(samples_amount):
            signal_collection[time] += generate_signal(amplitude, phase, frequency, time)
    return signal_collection
