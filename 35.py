import re
txt = 'ab abab abab abababab abea'
txt1 = re.findall(r'\b(ab)+\b', txt)
print(txt1)
