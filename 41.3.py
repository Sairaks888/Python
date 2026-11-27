import re
txt = 'xaz xBz xABz x12z'
print(re.findall(r'x[^A-Z]+z', txt))