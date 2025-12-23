#! python3
# Open all the product pages after searching a shopping site such as Amazon
import webbrowser, bs4, requests

amazonProductPage = requests.get('https://www.amazon.com/Razer-Nari-Essential-Wireless-Auto-Adjusting/dp/B07HZ5N8QT/ref=sr_1_1_sspa?keywords=gaming+headsets', headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
})
amazonProductPage.raise_for_status()
# get the unique product page
amazonSoup = bs4.BeautifulSoup(amazonProductPage.text, 'html.parser')
amazonElem = amazonSoup.select('.a-text-bold')

print(amazonElem)
print(amazonElem[0].get('href'))
for i in range(len(amazonElem)):
    webbrowser.open('https://www.amazon.com' + amazonElem[i].get('href'))