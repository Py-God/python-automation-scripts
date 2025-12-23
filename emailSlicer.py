#! python3
# analyses a user inputed email in a regex then seperates the username and domain name

import re

emailRegex = re.compile(r'(\w+)@(\w+.com)')

email = input('Type in your email: ')
mo = emailRegex.search(email)
if mo == None:
    print('That is not a valid email')
else:
    username = mo.group(1)
    domainName = mo.group(2)
    print('''Your username is '{}'
    Your domain name is '{}'
    '''.format(username, domainName))