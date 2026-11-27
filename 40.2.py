import re
txt = 'a1a a3a a7a a9a aba'
print(re.findall(r'a[3-6]a', txt))