import re

dateRegex = re.compile(r'(\d+)(-|/)(\d+)(-|/)(\d+)')
dateMatches = dateRegex.findall('12/12/2020 is a nice date. So is 12-12-2020. And 2015/12/12.')
matches = []
for date in dateMatches:
    date = list(date)
    date[1] = '-'
    date[3] = '-'
    newDates = ''.join(date)
    print(newDates)