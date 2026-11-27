import re
txt = 'ave a#b a2b a$b a4b a5b a-b acb'
txt1 = re.findall(r'a[^\w\s]b', txt)
print(txt1) 