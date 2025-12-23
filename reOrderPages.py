#! python3
# Reorder pages in a PDF.
import PyPDF2, random

file = open('meetingminutes.pdf', 'rb')
fileReader = PyPDF2.PdfFileReader(file)
newFile = PyPDF2.PdfFileWriter()
anotherNewFile = PyPDF2.PdfFileWriter()

randomList = [a for a in range(fileReader.numPages-1)]
for a in range(fileReader.numPages-1, -1, -1):
    page = fileReader.getPage(a)
    newFile.addPage(page)

for a in range(len(randomList)):
    pageNum = random.choice(randomList)
    page1 = fileReader.getPage(pageNum)
    anotherNewFile.addPage(page1)

new = open('reOrdered.pdf', 'wb')
new1 = open('reOrdered1.pdf', 'wb')
newFile.write(new)
anotherNewFile.write(new1)
new1.close()
new.close()
file.close()