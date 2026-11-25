def outer():
	i = 10

	def inner():
		nonlocal i
		i -= 2
		print(i)
	return inner
	
res1 = outer()
res1()
res1()

res2 = outer()
res2()
res2()
res2()