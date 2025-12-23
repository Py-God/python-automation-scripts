#! python3
# use regular expressions to read multiple formats of dates in a spreadsheet and edit them to
# a single, standard format
import re, openpyxl

print('Opening dates.xlsx...')
wb = openpyxl.load_workbook('dates.xlsx')
sheet = wb['Sheet1']

dateRegex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
print('Finding date matches...')
for date in sheet['A']:
    mo = dateRegex.search(str(date.value))
    if mo == None:
        continue
    else:
        firstPart = mo.group(1)
        secondPart = mo.group(2)
        thirdPart = mo.group(3)
    newDateFormat = firstPart + '.' + secondPart + '.' + thirdPart
    for i in range (1, sheet.max_row+1):
        sheet['A' + str(i)].value = newDateFormat
print('saving into new file: updatedDates.xlsx')
wb.save('updatedDates.xlsx')
