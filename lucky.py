#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
# the user may have searched for something that turned up fewer than five results.
# the number of tabs you want to open is either 5 or the length of this list (whichever is smaller).

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    # t the href attribute’s value in the returned <a> elements do not have the initial http://google.com part,
    # so you have to concatenate that to the href attribute’s string value.
