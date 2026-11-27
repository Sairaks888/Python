import re
txt = '1 23 456 789'
txt1 = re.search(r'\d{3}', txt)
print(txt1.start()) 