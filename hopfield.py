import numpy as np

class Hopfield:
    def __init__(self, patterns):
        self.patterns = {l: p.flatten() for l, p in patterns.items()}

        self.weights = np.zeros(self._pattern_size())
        for label, pattern in self.patterns.items():
            self.weights = self.weights + np.outer(pattern, pattern)
        self.weights[np.diag_indices(self._pattern_size())] = 0
        self.weights = self.weights / len(self.patterns)

    def _pattern_size(self):
        pattern = next(iter(self.patterns.values()))
        return len(pattern)

    def recall(self, pattern):
        return false
