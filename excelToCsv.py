#! pythom3
# a program that reads all the Excel files in the current working directory and outputs them as CSV files.
import csv, openpyxl, os

for excelFile in os.listdir('excelSpreadsheets'):
    # Skip non-xlsx files, load the workbook object.
    if excelFile.endswith('.xlsx'):
        print('converting %s' % excelFile +' to csv...')
        wb = openpyxl.load_workbook(os.path.join('excelSpreadsheets', excelFile))
        for sheetName in wb.sheetnames:
            # Loop through every sheet in the workbook.
            sheet = wb[sheetName]
            # Create the CSV filename from the Excel filename and sheet title.
            csvFilename = excelFile.rstrip('.xlsx') + '_' + sheetName + '.csv'
            # Create the csv.writer object for this CSV file.
            csvFile = open(os.path.join('excelSpreadsheets', csvFilename), 'w', newline='')
            csvWriter = csv.writer(csvFile)
            # Loop through every row in the sheet.
            for rowNum in range(1, sheet.max_row + 1):
                rowData = [] # append each cell to this list
                # Loop through each cell in the row.
                for colNum in range(1, sheet.max_column + 1):
                    # Append each cell's data to rowData.
                    data = sheet.cell(row=rowNum, column=colNum).value
                    rowData.append(data)
                # Write the rowData list to the CSV file.
                csvWriter.writerow(rowData)
            print('Done')
            csvFile.close()
    else:
        continue