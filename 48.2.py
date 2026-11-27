import re
txt = 'abc def xyz'
txt1 = re.findall(r'[a-z]+$', txt)
print(txt1)