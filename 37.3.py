import re

txt = 'aa aba abba abbba abbbba abbbbba'
txt1 = re.findall(r'\bab{4,}a\b', txt)
print(txt1)