#! python3
# Open the result links to photos after performing a search on a photo site such as Flickr or Imgur
import requests, bs4, sys, webbrowser

if len(sys.argv) > 1:
    print('googling '+ ' '.join(sys.argv[1:]) + ' on flickr...')
else:
    print('you did\'nt engage the customized line, try again')

photoPage = requests.get('https://www.flickr.com/search/?text=' + ''.join(sys.argv[1:]))
photoPage.raise_for_status()

pageSoup = bs4.BeautifulSoup(photoPage.text, 'html.parser')

photoSearch = pageSoup.select('.image a')
print(photoSearch)

photoNumber = min(len(photoSearch), 5)

for i in range(photoNumber):
    webbrowser.open('https://www.flickr.com/' + photoSearch[i].get('href'))
