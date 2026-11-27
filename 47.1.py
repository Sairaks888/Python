import re

txt = 'xaz xBz xcz x-z x@z'
txt1 = re.findall(r'x[a-zA-Z-]z', txt)
print(txt1)