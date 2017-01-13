import numpy as np

class Reader:
	label_size = 1

	def __init__(self, file_name):
		self.file_name = file_name

	def patterns(self):
		file = open(self.file_name, 'r')
		read_lines = file.read().splitlines()
		lines = list(filter(None, read_lines))
		self.pattern_size = int(lines[0])
		patterns = self._parse_patterns(lines[1:])
		return {'pattern_size': self.pattern_size, 'patterns': patterns}

	def _parse_patterns(self, patterns_lines):
		patterns = {}
		for i in range(0, len(patterns_lines), self.pattern_size + self.label_size):
			pattern_lines = patterns_lines[i:i + self.pattern_size + self.label_size]
			pattern = self._parse_pattern(pattern_lines)
			patterns.update(pattern)
		return patterns

	def _parse_pattern(self, pattern_lines):
		label = pattern_lines[0]
		pattern = pattern_lines[1:self.pattern_size + self.label_size]
		return { label: self._to_sgn(pattern) }

	def _to_sgn(self, pattern_lines):
		result = np.full((self.pattern_size, self.pattern_size), -1)
		for row_idx, row in enumerate(pattern_lines):
			for col_idx, char in enumerate(row):
				if char != ' ': result[row_idx][col_idx] = 1
		return result
