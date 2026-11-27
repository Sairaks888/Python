import re
txt = '456 aaa 123 b2bb 987'
res = re.finditer(r'\b(?P<first>\d)(?P<rest>\d+)\b', txt)
for el in res:
    print(el[0], el['first'], el['rest'])