def outer():
	def inner(num):
		return num + 2
	return inner	
res = outer()(3)
print(res)