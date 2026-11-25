num = 3
def outer():
	global num
	num += 1
	tst = num

	def inner():
		nonlocal tst
		tst = tst ** 3
	inner()
	return tst
print(outer())