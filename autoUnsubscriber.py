#! python3
# a program that scans through your email account, finds all the unsubscribe links in all your emails,
# and automatically opens them in a browser.
import webbrowser, imapclient, imaplib, pyzmail, bs4

imaplib.MAXLINE = 10000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print('logging into your gmail')
imapObj.login('boluwatifelekeoduoye@gmail.com', 'bajtcryceihnsxuj')
imapObj.select_folder('INBOX', readonly=True)
print('searching your messages')
UIDs = imapObj.gmail_search('unsubscribe')
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

for i in range(7):
    try:
        message = pyzmail.PyzMessage.factory(rawMessages[UIDs[i]][b'BODY[]'])
        if message.html_part != None:
            html = message.html_part.get_payload().decode(message.html_part.charset)
            print('searching for unsubscribe link...')
            htmlSoup = bs4.BeautifulSoup(html, 'html.parser')
            linkElem = htmlSoup.select('a')
            link = linkElem.get('href')
            webbrowser.open(link)
        else:
            continue
    except:
        continue