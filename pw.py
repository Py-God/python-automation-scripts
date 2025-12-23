#! python3
# pw.py - an insecure password locker program.

PASSWORDS = {'email': 'F318DJ1D91jdau93HhsiIJ21',
             'blog': 'VJSkjsBbihdKB738397839',
             'luggage': '12345'}


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: Python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]               # first command line arguement is the account name, account name is stored as a string

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
