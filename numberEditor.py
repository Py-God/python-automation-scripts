import re

text = '12 1,334 13,131 131,313 1342414 14114131'
editorRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
matches = editorRegex.findall(text)

print(matches)



