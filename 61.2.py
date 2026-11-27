import re
txt = 'site.ru sss site.com zzz site.net'
res = re.findall(r'([a-zA-Z0-9]+)\.([a-zA-Z]+)', txt)
print(res)