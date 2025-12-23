#! python3
# a program that runs just before you wake up in the morning and checks whether it’s raining that
# day. If so, have the program text you a reminder to pack an umbrella before leaving the house
import requests, bs4, textMyself

def weatherChecker():
    page = requests.get('https://www.weather-atlas.com/en/nigeria/lagos')
    page.raise_for_status()
    pageSoup = bs4.BeautifulSoup(page.text, 'html.parser')
    pageElem = pageSoup.select('#today')
    print(pageElem[0].getText())
    '''
    rainChance = pageElem[0].getText()
    if int(rainChance.rstrip('%')) >= 50:
        textMyself.textmyself('High chance of rain today. Grab an umbrella!')
    else:
        textMyself.textmyself('Low chance of rain today. make your choice.')'''

weatherChecker()