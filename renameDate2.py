#! python3
# renameDates.py - Renames filenames with European DD-MM-YYYY date format to American MM-DD-YYYY.

import shutil, os, re

# Create a regex that matches files with the European date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1|2|3)?\d)-                     # one or two digits for the day
((0|1)?\d)-                         # one or two digits for the month
((19|20)\d\d)                       # four digits for the year
(.*?)$                              # all text after the date
""", re.VERBOSE)
# all this is a regex to find files with dates on it e.g spam4-12-1984.txt and 31-01-2014eggs.zip

# Loop over the files in the working directory.
for euroFilename in os.listdir('.'):
    mo = datePattern.search(euroFilename)
# Skip files without a date.
    if mo.group() == None:
        continue
# Get the different parts of the filename.
beforePart = mo.group(1)
dayPart = mo.group(2)
monthPart = mo.group(4)
yearPart = mo.group(6)
afterPart = mo.group(8)

# Form the European-style filename.
amerFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart
# Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')
euroFilename = os.path.join(absWorkingDir, euroFilename)
amerFilename = os.path.join(absWorkingDir, amerFilename)
# Rename the files.
print('Renaming "%s" to "%s"...' % (euroFilename, amerFilename))
#shutil.move(amerFilename, euroFilename) # uncomment after testing