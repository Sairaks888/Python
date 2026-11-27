import re
txt = '''
	abc
	def
	ghi
	jkl
'''
txt1 = re.sub(r'$', '!', txt, flags=re.MULTILINE)
txt2 = re.sub(r'^|$', '!', txt1) 
print(txt1)

