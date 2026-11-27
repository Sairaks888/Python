import re
txt = 'wйw wяw wёw wqw'
txt1 = re.findall(r'w[а-яё]w', txt)
print(txt1)