import re
txt = 'aba aea aca aza axa'
print(re.findall(r'a[bex]a', txt))