import re
txt = 'abc !!! ?????? 123 @@@@ xyz'
txt1 = re.findall(r'[^\s\da-g]{3,7}', txt)
print(txt1)