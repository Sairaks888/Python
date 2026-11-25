def outer(lst):
	def inner(num):
		return num.capitalize()
	res = []
	for el in lst:
		res.append(inner(el))
	return res
print(outer(['яблоко, банан']))