#! python3
# Cut out specific pages from PDFs.
import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
newPDFfile = PyPDF2.PdfFileWriter()
for a in range(0, pdfReader.numPages, 3):
    page = pdfReader.getPage(a)
    newPDFfile.addPage(page)

nPdf = open('multipleOfThree.pdf', 'wb')
newPDFfile.write(nPdf)
nPdf.close()
pdfFile.close()