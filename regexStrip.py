import re

def regexStrip(char):
    whiteSpaceRegex = re.compile(r'^\s+\w+\s+$')
    matches = whiteSpaceRegex.search(char)
    if matches != None:
        match = matches.group()
        for letter in match:
            if letter == 'n':
                pass
        print(match)
    else:
        print('no whitespace characters at the start or end of this string')
        exit()

text = '    nnanana     '
regexStrip(text)