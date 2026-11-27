import re
txt = '123 abc 456 cde'
txt1 = re.search(r'[a-zA-Z]+', txt)
print(txt1[0]) 