#! python
#  a program that, given the URL of a web page, will attempt to download every linked page on the page.
# The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
# this program also does the backup web project
import requests, bs4, os

print('Making the Nairaland backup folder in your directory...')
os.makedirs('Nairaland_HomePage_backup', exist_ok=True)

print('Downloading the Nairaland home page...')
webPage = requests.get('https://www.nairaland.com/')
webPage.raise_for_status()

webSoup = bs4.BeautifulSoup(webPage.text, 'html.parser')
linkElem = webSoup.select('a')

d = 1
for i in range(len(linkElem)):
    link =  linkElem[i].get('href')
    try:
        if link.startswith('/'):
            link = 'https://www.nairaland.com' + link
            print('Downloading %s.' % link)
            page = requests.get(link)
            try:
                page.raise_for_status()
                pageFile = open(os.path.join('Nairaland_HomePage_backup','%s.txt' % d), 'wb')
                for chunk in page.iter_content(100000):
                    pageFile.write(chunk)
                pageFile.close()
                d = d+1
            except:
                print('something went wrong while downloading')
        elif link.startswith('https'):
            print('downloading %s.' % link)
            page = requests.get(link)
            try:
                page.raise_for_status()
                pageFile = open(os.path.join('Nairaland_HomePage_backup', '%s.txt' % d), 'wb')
                for chunk in page.iter_content(100000):
                    pageFile.write(chunk)
                pageFile.close()
                d +=1
            except:
                print('something went wrong while downloading')
        elif link == 'https://www.nairaland.com/':
            continue
        else:
            print('Broken link.')
            continue
    except:
        continue
print('Done')