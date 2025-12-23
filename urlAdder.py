#! python3
# Adds text or a website URL to images.

import os
from PIL import Image

logofile = Image.open('480px-Facebook_f_logo_(2021).svg.png')
logofile = logofile.resize((50, 50))
logoWidth, logoHeight = logofile.size
for file in os.listdir('.'):
    if file.endswith('.png') or file.endswith('.jpg') and not file.endswith('480px-Facebook_f_logo_(2021).svg.png'):
        im = Image.open(file)
        imWidth, imHeight = im.size
        print('adding logo to %s' % file)
        im.paste(logofile, (imWidth - logoWidth, imHeight - logoHeight), logofile)
        im.save(os.path.join('facebookLogoAdded', file))
    else:
        continue