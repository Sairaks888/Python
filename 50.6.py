import re
txt = '''
	abc
	def
	ghi
	jkl
'''
txt1 = re.sub(r'^(\t)', r'!\1', txt, flags=re.MULTILINE)
print(txt1)

