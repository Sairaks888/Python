import re
txt = 'aaa 123 bbb 456 987'
res = re.finditer(r'(\d)(\d)(\d)', txt)
for el in res:
    print(el[0], el[1], el[2], el[3])