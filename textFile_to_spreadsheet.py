#! python3
#  a program to read in the contents of several text files (you can make the text files yourself) and insert
# those contents into a spreadsheet, with one line of text per row.
import openpyxl, os

files = os.listdir('C:\\Users\\user\\Desktop\\PYTHON\\textFiles')
wb = openpyxl.Workbook()
sheet = wb.active
b = 1
for file in files:
    filepath = os.path.join('C:\\Users\\user\\Desktop\\PYTHON\\textFiles', file)
    cont = open(filepath)
    content = cont.readlines()
    for row in range(1, len(content)+1):
        sheet.cell(row=row, column=b).value = content[row-1].rstrip('\n')
    b+=1
wb.save('txtToSpreadsheet.xlsx')

