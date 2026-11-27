import re
txt = 'aeeea aeea aea axa axxa axxxa'
txt1 = re.findall(r'a(?:e+|x+)a', txt)
print(txt1)