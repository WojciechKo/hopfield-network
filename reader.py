import numpy as np

LABEL_SIZE = 1

def read_patterns():
	file = open('patterns', 'r')
	read_lines = file.read().splitlines()
	lines = list(filter(None, read_lines))
	pattern_size = int(lines[0])
	patterns = _parse_patterns(pattern_size, lines[1:])
	return {'pattern_size': pattern_size, 'patterns': patterns}

def _parse_patterns(pattern_size, patterns_lines):
	patterns = {}
	for i in range(0, len(patterns_lines), pattern_size + LABEL_SIZE):
		pattern_lines = patterns_lines[i:i + pattern_size + LABEL_SIZE]
		pattern = _parse_pattern(pattern_size, pattern_lines)
		patterns.update(pattern)
	return patterns

def _parse_pattern(pattern_size, pattern_lines):
	label = pattern_lines[0]
	pattern = pattern_lines[1:pattern_size + LABEL_SIZE]
	return { label: _to_sgn(pattern_size, pattern) }

def _to_sgn(pattern_size, pattern_lines):
	result = np.full((pattern_size, pattern_size), -1)
	for row_idx, row in enumerate(pattern_lines):
		for col_idx, char in enumerate(row):
			if char != ' ': result[row_idx][col_idx] = 1
	return result
