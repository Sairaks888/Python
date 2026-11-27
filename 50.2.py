import re
txt = '''
	abc
	def
	ghi
	jkl
'''
txt1 = re.sub(r'^', '!', txt, flags=re.MULTILINE)
print(txt1)