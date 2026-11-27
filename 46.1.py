import re
txt = '^xx axx ^zz bkk @ss'
txt1 = re.findall(r'[\^@][a-zA-Z]{2}', txt)
print(txt1)