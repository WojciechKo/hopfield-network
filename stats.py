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

def generate_patterns(patterns_count, size):
    return dict([generate_pattern(i, s) for i, s in enumerate([size] * patterns_count)])

hopfield = Hopfield(generate_patterns(10, 10))
