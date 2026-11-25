def func(num1, num2, *, num3):
	return (num1 + num2) * num3
	
print(func(2, 4, num3=3))