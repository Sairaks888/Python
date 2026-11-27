import re
txt = '''
	abc
	def
	ghi
	jkl
'''
txt1  = re.sub(r'^|$', '!', txt) 
print(txt1)