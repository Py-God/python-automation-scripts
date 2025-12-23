#! python3
# Create a PDF from only those pages that have some specific text
import PyPDF2

file = open('meetingminutes.pdf', 'rb')
fileReader = PyPDF2.PdfFileReader(file)
newFile = PyPDF2.PdfFileWriter()
for numPage in range(fileReader.numPages):
    page = fileReader.getPage(numPage)
    if 'seconded' in page.extract_text():
        newFile.addPage(page)
    else:
        continue

new_File = open('specificPages.pdf', 'wb')
newFile.write(new_File)
new_File.close()
file.close()