import re
txt = 'abcde'
res = re.fullmatch(r'[a-zA-Z]+', txt)
if res:
    print("состоит только из букв")
else:
    print("состоит не только из букв")