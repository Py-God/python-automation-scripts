# a program that finds all files with a given prefix, such as spam001.txt,
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the
# program rename all the later files to close this gap
import shutil, os, re

def fillInTheGaps(folder):
    folder = os.path.abspath(folder)

    errorRegex = re.compile(r'(\D*)(\d+)(.*)')

    for foldername, subfolder, files in os.walk(folder):
        for file in files:
            mo = errorRegex.search(os.path.join(foldername, file))
            if mo == None:
                continue
            else:
                beforePart = mo.group(1)
                numberPart = mo.group(2)
                afterPart = mo.group(3)
            print(numberPart.lstrip('00'))

fillInTheGaps('C:\\eggs')