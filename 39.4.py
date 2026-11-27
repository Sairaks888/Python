import re
txt = 'avb a1b a2b a3b a4b a5b abb acb'
txt1 = re.findall(r'a[^\d\s]b', txt)
print(txt1) 