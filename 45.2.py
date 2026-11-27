import re
txt = 'x[]z x{}z x.z x()z x([])z'
txt1 = re.findall(r'x[\[\](){}.*]+z', txt) 
print(txt1)