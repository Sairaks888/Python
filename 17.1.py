def func(num):
	return num + 1

lst = [1, 2, 3, 4, 5]
res = map(lambda num: num +1, lst)
print(list(res))