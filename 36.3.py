import re
txt = '23 2+3 2++3 2+++3 345 567'
txt1 = re.findall(r'\b2(?:\+)+3\b', txt)
print(txt1)