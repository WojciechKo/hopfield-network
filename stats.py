import numpy as np
from hopfield import Hopfield
from reader import Reader

def generate_pattern_array(size):
    pattern = np.random.randint(2, size=(size, size))
    pattern[pattern == 0] = -1
    return pattern

def generate_pattern(index, size):
    label = "pattern-" + str(index)
    return [label, generate_pattern_array(size)]

def train_hopfield(patterns_count, size):
    patterns = dict([generate_pattern(i, s) for i, s in enumerate([size] * patterns_count)])
    return Hopfield(patterns)

hopfield = train_hopfield(10, 10))
