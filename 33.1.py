import re

txt = 'ahb acb aeb aeeb adcb axeb'
txt1 = re.sub('a.b', '!', txt)
print(txt1)