#! python3
# Copy or move images into different folders based on their sizes.

import os, shutil, sys

print(sys.executable)
for file in os.listdir('.'):
    if file.endswith('.png') or file.endswith('.jpg'):
        if os.path.getsize(file) > 1024:
            print('%s greater than 1mb' % file)
            shutil.copy(file, 'images greater than 1mb')
        else:
            print('%s less than 1mb' % file)
            shutil.copy(file, 'images less than 1mb')
    else:
        continue