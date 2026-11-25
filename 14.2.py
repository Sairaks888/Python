def func(num1, *, num2, num3):
	return (num1 - num2) / num3
	
print(func(12, 4, num3=5))