# To remove the zeros from files such as spam0042.txt

import shutil, os, re

zeroRegex = re.compile(r'''^(.*?)   # everything before the zero
(0+)                                # the zero
(.*?)$                               # everything after the zero
''', re.VERBOSE)

filePath = os.path.join('C:\\bacon_backup')
for filenames in os.listdir(filePath):
    mo = zeroRegex.search(filenames)
    if mo == None:
        pass
    else:
        fil = mo.group()
        beforePart = mo.group(1)
        zeropart = mo.group(2)
        afterPart = mo.group(3)

newFileName = beforePart + afterPart
newFilePath = os.path.join(filePath, newFileName)
print('renaming %s to %s' % (fil, newFileName))
# shutil.move(file, newFilePath)
