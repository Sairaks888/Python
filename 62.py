import re
txt = '12 aaa 34 bbb 56 ccc'
res = re.finditer(r'\d+', txt)
for el in res:
    print(el[0])