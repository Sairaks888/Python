def func(num, clb):
	return clb(num)
print( func(2, lambda num: + 1))