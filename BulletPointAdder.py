#! python3
# bulletPointAdder.py - adds wikipedia bulletpoints to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# TODO: seperate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # Add star to each string in the 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)
