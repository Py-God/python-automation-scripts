import re

name = re.compile(r'([A-Z][a-z]+ Nakamoto)')
text = 'Satoshi Nakamoto, Robocop Nakamoto satoshi nakamoto Nakamoto nakamoto'
names = name.findall(text)
print(names)