import re
txt = 'http://domain.ru'
res = re.search(r'(\w+)://([a-zA-Z0-9]+)\.([a-zA-Z]+)', txt)
print(res.groups())