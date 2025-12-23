#! python3
# Collect writeups from blog sites and save them as .txt files with the topic of the blog as the name of the file
# and the content of the topic as the content of the .txt file.
import requests, bs4, os

print('Creating \'Copy_Blogger\' folder in your main directory...')
os.makedirs('Copy_Blogger', exist_ok=True)

blogSite = requests.get('https://copyblogger.com/')
blogSite.raise_for_status()

blogSoup = bs4.BeautifulSoup(blogSite.text, 'html.parser')
blogElem = blogSoup.select('.entry-title-link')

for i in range(len(blogElem)):
    try:
        heading = blogElem[i].get_text()
        print('Creating ' + heading + '.txt' + '... in \'Copy_Blogger\' folder...')
        file = open(os.path.join('Copy_Blogger', heading + '.txt'), 'w')

        link = blogElem[i].get('href')
        print('Getting the article link...')
        blogContent = requests.get(link)
        blogContent.raise_for_status()

        contentSoup = bs4.BeautifulSoup(blogContent.text, 'html.parser')
        contentElem = contentSoup.select('.entry-content')
        content = contentElem[0].getText()
        file.write(content)
        file.close()
    except:
        print('Could\'nt create ' + heading + '.txt!')
        continue
print('Done')

