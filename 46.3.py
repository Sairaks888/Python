import re
txt = '^xx axx ^zz bkk'
txt1 = re.findall(r'[^\^\s][a-zA-Z]{2}', txt)
print(txt1)
