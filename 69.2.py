import re
txt = 'aaa @@@ 123w'
res = re.subn(r'[^\w\s]+', '!', txt)
print(res)