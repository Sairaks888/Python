import re
txt = 'func1() func2() func3()'
res = re.findall(r'\w+(?=\(\))', txt)
print(res)