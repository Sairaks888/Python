import re
txt = '12:37 15:48 17:59'
res = re.findall(r'(\d{2}):(\d{2})', txt)
print(res)
