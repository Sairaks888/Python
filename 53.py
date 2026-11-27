import re
txt = 'abcde 123456'
txt1 = re.search(r'[a-zA-Z]+', txt)
print(txt1.start()) 
print(txt1.end())   