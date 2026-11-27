import re

txt = 'aba aca aea abba adcb abea' 
txt1 = re.sub('a..a', '!', txt)
print(txt1)