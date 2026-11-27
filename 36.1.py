import re
txt = 'a.a aba aea'
txt1 = re.findall(r'a\.a', txt)
print(txt1)