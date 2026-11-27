import re
txt = 'a1a a2a a3a a4a a5a aba aca'
txt1= re.findall(r'a\da', txt)
print(txt1)