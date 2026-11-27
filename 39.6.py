import re
txt = 'ave a#a a2a a$a a4a a5a a-a aca'
txt1= re.sub(r'\s', '!', txt)
print(txt1) 