# a program that walks through a folder tree and searches for exceptionally
# large files or folders—say, ones that have a file size of more than 100MB.
# Print these files with their absolute path to the screen
import os

def unNeededFiles(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, files in os.walk(folder):
        print('Searching for files greater than 100mb in %s' % (foldername))
        for file in files:
            fileSize = os.path.getsize(os.path.join(foldername, file))
            if fileSize > 102400:
                print(os.path.join(foldername, file) + ' ----- ' + str(fileSize) + 'bytes' + '\n')

unNeededFiles('C:\\Games')