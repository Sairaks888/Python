import re
txt = 'sss domain.ru zzz'
res = re.search(r'([a-zA-Z0-9]+)\.([a-zA-Z]+)', txt)
print(res[1]) 
print(res[2]) 