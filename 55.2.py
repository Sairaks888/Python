import re
txt = '123 aaabbbccc'
res = re.search(r'(a+)(b+)(c+)', txt)
print(res.group(1)) 
print(res.group(2)) 
print(res.group(3))