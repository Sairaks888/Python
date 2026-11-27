import re
txt = 'alex23'
res = re.search(r'(?P<name>[a-zA-Z]+)(?P<age>\d+)', txt)
print(res.groupdict())