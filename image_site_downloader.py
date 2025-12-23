#! python3
# a program that goes to a photo-sharing site like Flickr or Imgur, searches
# for a category of photos, and then downloads all the resulting images
import requests, bs4, os

os.makedirs('imgur', exist_ok=True)
search = input('input your search: ')
print('searching for ' + search + ' on imgur...')
imgurSearch = requests.get('https://imgur.com/search?q=' + search)
imgurSearch.raise_for_status()

imgurSoup = bs4.BeautifulSoup(imgurSearch.text, 'html.parser')

photoElem = imgurSoup.select('.image-list-link img')

i = 0
s = 1
print('Downloading dog photos...')
while i < (5):
    imageLink = photoElem[i].get('src')
    print(imageLink)
    photo = requests.get('https:' + imageLink)

    photos = open(os.path.join('imgur', 'dogImage%s.jpg' % s), 'wb')

    for chunk in photo.iter_content(100000):
        photos.write(chunk)
        i = i+1
        s+=1
photos.close()
