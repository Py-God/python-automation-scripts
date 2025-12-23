# To add a prefix to the start of the filename, such as adding spam_ to rename eggs.txt to spam_eggs.txt

import os, shutil

for filenames in os.listdir('C:\\bacon'):   # loopin through all the files in a particular directory
    newName = 'spam_' + filenames   # this is what the newName is. stored in a variable to make it easier
    filePath = os.path.join('C:\\bacon', filenames)
    newFilePath = os.path.join('C:\\bacon', newName)
    # getting the file path of both the new and old name files

    print('Renaming %s to %s...' % (filenames, newName))
    newFile = shutil.move(filePath, newFilePath)