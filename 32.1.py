lst = ['a', 'b', 'c', 'd', 'e']
lst1 = {value: index + 1 for index, value in enumerate(lst)}
print(lst1)