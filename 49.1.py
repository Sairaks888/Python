import re
txt = 'abc def xyz'
txt1 = re.sub(r'\b', '#', txt)
print(txt1)