lst = ['abcd', 'ab', 'c', 'de', 'bc']
res = filter(lambda s: len(s) == 2, lst)
print(list(res))