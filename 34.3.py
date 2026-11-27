import re
txt = 'aa aba abba abbba abca abea'
txt1 = re.findall(r'\bab?a\b', txt)
print(txt1)