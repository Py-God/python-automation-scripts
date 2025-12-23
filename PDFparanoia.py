#! python3
# write a script that will go through every PDF in a folder (and its subfolders) and encrypt the PDFs using a
# password provided on the command line
import os, PyPDF2, send2trash

def encrypter(password, foldername):
    print('Engaging the encrypter.')
    for folder, subfolder, filename in os.walk(foldername):
        print('searching for PDF file in %s' % folder)
        for file in filename:
            if file.endswith('.pdf'):
                print('found %s.'% file)
                pdfFile = open(os.path.join(foldername, file), 'rb')
                pdfFileReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfFileReader.isEncrypted == True:
                    print('pdf file, %s is already encrypted, skipping...' % file)
                    continue
                else:
                    newPdf = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfFileReader.numPages):
                        pageObj = pdfFileReader.getPage(pageNum)
                        newPdf.addPage(pageObj)

                    print('encrypting %s' % file)
                    newPdf.encrypt(password)
                    newPdfFile = open(os.path.join('encrypted PDFs', file+'_encrypted.pdf'), 'wb')
                    print('saving %s as %s_encrypted.pdf' %(file, file))
                    newPdf.write(newPdfFile)
                    pdfFile.close()
                    newPdfFile.close()
            else:
                continue
    print('successfully encrypted all PDFs in %s' % foldername)

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
                        pdfFile.close()
                    except:
                        print('Password incorrect for %s' % file)
                else:
                    continue
            else:
                continue

def deleteFormerPdfs():
    try:
        decryptPdfs('encrypted PDFs', passwrd)
        send2trash.send2trash('PDF folder')
    except:
        print('Something went wrong while trying to decrypt the files in encrypted PDFs folder.')

passwrd = input('Enter the password to be used for the files:\n')
encrypter(passwrd, 'PDF folder')
deleteFormerPdfs()