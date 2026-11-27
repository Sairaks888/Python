import re
txt = 'abc def xyz'
txt1 = re.sub(r'\B', '+', txt)
print(txt1)