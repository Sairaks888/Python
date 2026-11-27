import re
txt = '2+3 223 2223'
txt1 = re.findall(r'2\+3', txt)
print(txt1)