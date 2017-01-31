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

def try_to_recall(hopfield, pattern_to_recall, tries = 20):
    result = {}
    pattern = pattern_to_recall
    for i in range(tries):
        result = hopfield.recall(pattern)
        pattern = result["pattern"]
        if result["stable"] or result["name"]: return result

    return result

def corrupt_pattern(name, original_pattern, percentage):
    pattern = np.copy(original_pattern)
    count = int(pattern.size * percentage)
    chosen = np.random.choice(range(pattern.size), count, replace=False)
    for index in chosen:
        pattern[index] *= -1
    return (name, pattern)

def test_pattern(hopfield, name, pattern):
    result = try_to_recall(hopfield, pattern)
    return 1 if result["name"] == name else 0

def test_hopfield(hopfield):
    corruptions = np.arange(0, 0.5, 0.05)
    iterations = 5
    results = np.empty((corruptions.size, 2))
    for idx, corruption in enumerate(corruptions):
        corruption_results = np.zeros(iterations)
        for i in range(iterations):
            result = [test_pattern(hopfield, *corrupt_pattern(*pattern, corruption)) for pattern in hopfield.patterns.items()]
            corruption_results[i] = np.average(result)
        results[idx] = [corruption, np.median(corruption_results)]
    return results

network_size = 900
pattern_size = int(np.sqrt(network_size))

network_fullness = np.arange(0.05, 0.15, 0.01)
for fullness in network_fullness:
    print("Fullness: " + str(fullness))

    patterns_count = int(network_size * fullness)
    patterns = generate_patterns(patterns_count, pattern_size)
    hopfield = Hopfield(patterns)

    results = test_hopfield(hopfield)
    for corruption, result in results:
        print("Corruption: " + '{:.1%}'.format(corruption), end="\t")
        print("Result: " + '{:.1%}'.format(np.average(result)))
    print("\n")
