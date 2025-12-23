#! python3
# a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF
# using a provided password.
import PyPDF2, os

def decryptPdfs(folder, password):
    print('engaging the decrypter')
    for foldername, subfolder, files in os.walk(folder):
        print('searching for encrypted PDF files in %s' % folder)
        for file in files:
            if file.endswith('_encrypted.pdf'):
                print('found %s' % file)
                pdfFile = open(os.path.join(folder, file), 'rb')
                pdfFileReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfFileReader.isEncrypted == True:
                    print('Decrypting %s...' % file)
                    pdfFileReader.decrypt(password)
                    try:
                        pdfFileReader.getPage(0)
                        print('successfully decrypted %s' % file)
                        newPdf = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfFileReader.numPages):
                            pageObj = pdfFileReader.getPage(pageNum)
                            newPdf.addPage(pageObj)
                        newPdfFile = open(os.path.join('unEncrypted_Pdfs', file.replace('_encrypted', '')), 'wb')
                        print('saving %s as %s' %(file, file.replace('_encrypted', '')))
                        newPdf.write(newPdfFile)
                        pdfFile.close()
                        newPdfFile.close()
                    except:
                        print('Password incorrect for %s' % file)
                else:
                    continue
            else:
                continue
decryptPdfs('encrypted PDFs', 'BoluBabs')