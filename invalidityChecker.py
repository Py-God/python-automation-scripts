#! python3
# Check whether a spreadsheet has blank rows or invalid data in any cells and alert the user if it does.
import openpyxl

print('Opening workbook...')
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

def blankRows():
    print('reading rows...')
    rows = sheet['A1':'C7']
    columns = sheet[1]
    for row in rows:
        for r in row:
            if r.value == None:
                print('blank row found at ' + r.coordinate)
            else:
                continue
    for column in columns:
        if column.value == None:
            print('blank column found at ' + column.coordinate)
        else:
            continue

    print('Done')

blankRows()
