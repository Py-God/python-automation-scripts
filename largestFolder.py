#! python3
# Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space

import os

folderSizeList = []
def largeFolder1(folder):
    # find the largest folder in a directory tree - one that uses the most disk space
    filePath = os.path.abspath(folder)
    for foldername, subfolders, files in os.walk(filePath):
        for subfolder in subfolders:
            print('Searching for the largest folder in %s' % (subfolder))
            folderSize = os.path.getsize(os.path.join(folder, subfolder))
            folderSizeList.append(folderSize)
            largestFolderSize = max(folderSizeList)

        print(largestFolderSize)
        largestFolder = subfolders[folderSizeList.index(largestFolderSize)]

    print('the largest folder  in %s is ' + largestFolder + ' ----- ' + str(largestFolderSize) + 'bytes' + '\n' % (folder))

largeFolder1('C:\\Users\\user\\Desktop\\PYTHON')