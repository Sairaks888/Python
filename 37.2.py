import re
txt = 'aa aba abba abbba abbbba abbbbba'
txt1 = re.findall(r'\bab{1,3}a\b', txt)
print(txt1)