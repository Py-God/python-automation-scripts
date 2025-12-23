import re

passwordRegex = re.compile(r'[a-zA-Z0-9]+')
password = 'asSsA122'
match = passwordRegex.search(password).group()
if len(match) < 8:
    print('Your password is not long enough.')
else:
    print('PASSWORD SAVED')