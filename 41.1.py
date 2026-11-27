import re
txt = '1a2 1e2 1x2 1b2'
print(re.findall(r'1[^ex]2', txt))