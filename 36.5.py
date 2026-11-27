import re
txt = '*+ *q+ *qq+ *qqq+ *qqq qqq+'
txt1 = re.findall(r'\*q+\+', txt)
print(txt1)
