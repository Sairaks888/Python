import re
txt = 'code.mu 1234'
res = re.match(r'([a-zA-Z0-9]+)\.([a-zA-Z]+)', txt)
print(res[1]) 
print(res[2]) 