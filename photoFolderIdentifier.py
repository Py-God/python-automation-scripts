#! python3 #
#  a program that goes through every folder on your hard drive and finds potential photo folders.
import os
from PIL import Image

print('Going through all folders in your directory...')
for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        try:
        # Check if file extension isn't .png or .jpg.
            if not (filename.endswith('.png') or filename.endswith('.jpg')):
                numNonPhotoFiles += 1
                continue # skip to next filename
            else:
                # Open image file using Pillow.
                im = Image.open(os.path.join(foldername, filename))
                # Check if width & height are larger than 500.
                width, height = im.size
                if int(width) > 500 and int(height) > 500:
                    # Image is large enough to be considered a photo.
                    numPhotoFiles += 1
                else:
                    # Image is too small to be a photo.
                    numNonPhotoFiles += 1
        except:
            continue
    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(foldername)