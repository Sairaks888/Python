import re
txt = 'abc 123 bbb 456 987'
res = re.match(r'[a-zA-Z]+', txt)
print(res[0]) 