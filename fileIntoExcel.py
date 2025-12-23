#! python3
# Read data from websites, text files, or the clipboard and write it to a spreadsheet.
import openpyxl

print('reading excelFile and excelFile2...')
file1 = open('excelFile.txt')
file2 = open('excelFile2.txt')
text1 = file1.read()
text2 = file2.read()
text1Content = text1.split()
text2Content = text2.split()

wb = openpyxl.Workbook()
sheet = wb['Sheet']
print('Appending the content of both files to an excel file...')
b = 0
for i in range(1, len(text1Content)+1):
    sheet['A' + str(i)].value = text1Content[b]
    sheet['B' + str(i)].value = text2Content[b]
    b+=1
print('saving the excel file to newExcelFile3.xlsx...')
wb.save('newExcelFile3.xlsx')
