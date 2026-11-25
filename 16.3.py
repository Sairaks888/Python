def func(num1, num2, clb):
	return clb(num1) + num2	
print(func(2, 6, lambda num: num **3))