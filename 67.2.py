import re
txt = 'aaa bbb 123'
res = re.match(r'.*?(\d+)', txt)
print(res[1]) 