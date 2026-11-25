def func(num, clb1, clb2):
	return clb1(num), clb2(num)
print(func(2, lambda num: num + 1, lambda num: num - 1))