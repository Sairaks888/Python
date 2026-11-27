import re
txt = 'aAa aea aEa aJa a3a'
print(re.findall(r'a[a-fA-D]a', txt))