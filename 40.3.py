import re
txt = 'aba aea afa aha aga'
print(re.findall(r'a[a-g]a', txt))