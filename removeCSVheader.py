#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current working directory.
import csv, os

os.makedirs('headerRemoved', exist_ok=True)
# Loop through every file in the current working directory.
for csvFilename in os.listdir('removeCSVheader'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files
    else:
        print('Removing header from ' + csvFilename + '...')
        # TODO: Read the CSV file in (skipping first row).
        csvFileObj = open(os.path.join('removeCSVheader', csvFilename))
        csvFileObj1 = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
        readerObj = csv.reader(csvFileObj)
        csvWriter = csv.writer(csvFileObj1)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue # skip first row
            else:
            # TODO: Write out the CSV file.
                csvWriter.writerow(row)
        csvFileObj1.close()
        csvFileObj.close()

