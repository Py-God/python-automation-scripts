import re

urlRegex = re.compile('''https*://(www.\w+.com)/''')
urlMatches = urlRegex.findall('''http://www.basmati.com/ is my favorite site. so is https://www.manana.com/''')
for urls in urlMatches:
    print(urls)