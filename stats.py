import numpy as np
from hopfield import Hopfield
from reader import Reader

def generate_pattern_array(size):
    pattern = np.random.randint(2, size=(size, size))
    pattern[pattern == 0] = -1
    return pattern

def generate_patterns(patterns_count, size):
    generate_pattern = lambda i, s: ("pattern-" + str(i), generate_pattern_array(s))
    return dict([generate_pattern(i, s) for i, s in enumerate([size] * patterns_count)])


def try_to_recall(pattern_to_recall, tries):
    result = {}
    pattern = pattern_to_recall
    for i in range(tries):
        result = hopfield.recall(pattern)
        pattern = result["pattern"]
        print(i)
        if result["stable"] or result["name"]: return result

    return result

patterns_count = 10
pattern_size = 10

patterns = generate_patterns(patterns_count, pattern_size)
hopfield = Hopfield(patterns)
init_pattern = generate_pattern_array(pattern_size)

new_pattern = init_pattern

result = try_to_recall(init_pattern, 10)

print(result["stable"])
print(result["name"])
