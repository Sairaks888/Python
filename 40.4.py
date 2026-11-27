import re
txt = 'aba aea afa aha aga'
print(re.findall(r'a[a-fj-z]a', txt))