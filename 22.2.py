def outer():
	def inner(txt):
		return 'hello, ' + txt
	return inner
res = outer()
print(res)