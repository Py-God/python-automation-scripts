#! python3
# Copy specific data from a CSV file to an Excel file, or vice versa.
import openpyxl, csv

csvFile = open('example.csv')
csvReader = csv.reader(csvFile)
excelFile = openpyxl.Workbook()
sheet = excelFile.active

b = 1
for row in csvReader:
    if csvReader.line_num != 3:
        for col in range(len(row)):
            sheet.cell(row=b, column=col+1).value = row[col]
        b+=1
    else:
        break
excelFile.save('csv.xlsx')
