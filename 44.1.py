import re
txt = '123.45 abc 1.2.3 @@@ .'
txt1 = re.findall(r'[\d.]+', txt)
print(txt1)