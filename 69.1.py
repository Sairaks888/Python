import re
txt = 'aaa bbb 123 www'
res = re.subn(r'[a-zA-Z]+', '!', txt)
print(res)