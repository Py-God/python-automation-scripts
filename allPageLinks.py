#! python3
# Opens all links on a page in separate browser tabs.
import webbrowser, re

urlRegex = re.compile(r'http://\S+/')
urlMatches = urlRegex.findall('https://www.reddit.com/')
for urls in urlMatches:
    webbrowser.open(urls)