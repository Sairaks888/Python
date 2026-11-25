data = {
	'a': {
		'b': 1,
		'c': 2,
		'd': {
			'e': 3,
			'f': 4
		}
	},
	'j': {
		'h': 5,
		'k': 6,
	},
	'l': 7
}
def get_numbers(d):
    res = []
    for value in d.values():
        if isinstance(value, dict):
            res.extend(get_numbers(value))
        elif isinstance(value, (int, float)):
            res.append(value)
    return res
print(get_numbers(data))