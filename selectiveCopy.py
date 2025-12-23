# Write a program that walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder
import os, shutil

def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    # makes sure its absolute
    for foldername, subfolders, files in os.walk(folder):
        print('finding .py and .jpg files in %s' % (foldername))
        for file in files:
            if file.endswith('.py') or file.endswith('.jpg'):
                print('copying %s from %s to C:\\eggs folder...' % (file, foldername))
                shutil.copy(os.path.join(foldername, file), 'C:\\eggs')
            else:
                continue

selectiveCopy('C:\\bacon_backup')