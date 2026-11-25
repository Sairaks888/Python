num = 10
def outer():
	num = 5
	def inner():
		nonlocal num
		num -= 2
	inner()
	return num
print(outer())