import re
txt = 'aba aea aca aza axa a.a a+a a*a'
txt1 = re.findall(r'a[.+*]a', txt)
print(txt1)