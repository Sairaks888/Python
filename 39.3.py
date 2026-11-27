import re
txt = 'aa a1a a22a a333a a4444a a55555a aba aca'
txt1 = re.findall(r'a\d*a', txt)
print(txt1) 