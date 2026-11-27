import re
txt = 'aba accca azzza wwwwa'
txt1 = re.sub(r'a.+?a', '!', txt)
print(txt1)