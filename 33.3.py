import re
txt = 'aba aca aea abba adca abea'
txt1 = re.findall(r'\bab.a\b', txt)
print(txt1)