import numpy as np
import random

class Hopfield:
    def __init__(self, patterns):
        self.patterns = {l: p.flatten() for l, p in patterns.items()}
        self._train()

    def _train(self):
        self.weights = np.zeros(self._pattern_size())
        for label, pattern in self.patterns.items():
            self.weights = self.weights + np.outer(pattern, pattern)
        self.weights[np.diag_indices(self._pattern_size())] = 0
        self.weights = self.weights / len(self.patterns)

    def _pattern_size(self):
        pattern = next(iter(self.patterns.values()))
        return len(pattern)

    def recall(self, pattern):
        sgn = lambda x: -1 if x<0 else 1
        new_pattern = np.zeros(pattern.flatten().shape)
        points = list(range(pattern.size))
        random.shuffle(points)
        for point_index in points:
            new_pattern[point_index] = sgn(np.dot(pattern.flatten(),self.weights[point_index]))
        return {"pattern": new_pattern.reshape(pattern.shape)}
