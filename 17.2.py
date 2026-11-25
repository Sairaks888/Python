def func(txt):
	return txt[::-1]
lst = ['123', '456', '789']
res = map(lambda txt: txt [::-1], lst)
print(list(res))