#! python3
#  a program that will decrypt the PDF by trying every possible English word until it finds one that works.
import PyPDF2

pdfFile = open('encrypted.pdf', 'rb')
pdfFileReader = PyPDF2.PdfFileReader(pdfFile)
passwordFile = open('dictionary.txt')
passwordList = passwordFile.readlines()
print('trying all possible passwords...')
for passwordNum in range(len(passwordList)):
    pdfFileReader.decrypt(passwordList[passwordNum])
    try:
        pdfFileReader.getPage(0)
        print('Password found!: %s' % (passwordList[passwordNum]))
    except:
        pdfFileReader.decrypt(passwordList[passwordNum].lower())
        try:
            pdfFileReader.getPage(0)
            print('Password found!: %s' % (passwordList[passwordNum]))
        except:
            continue

pdfFile.close()
print('Done')