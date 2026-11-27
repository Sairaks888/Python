lst1 = ['name1', 'name2', 'name3', 'name4']
lst2 = ['john', 'kate', 'alex', 'mary']
lst3 = {key: value for key, value in zip(lst1, lst2)}
print(lst3)